#!/usr/bin/env python3
"""Read-only evidence-record checks. Does NOT determine factual truth."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlsplit

LIMIT = 4 * 1024 * 1024
PASS = 'MECHANICAL_CHECKS_PASSED_NEEDS_SEMANTIC_REVIEW'
KINDS = {'fact', 'inference', 'advice', 'opinion', 'fiction', 'uncertainty', 'other'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def read_utf8(path):
    require(path.is_file(), f'Not a regular file: {path.name}')
    with path.open('rb') as handle:
        raw = handle.read(LIMIT + 1)
    require(len(raw) <= LIMIT, f'File exceeds 4 MiB: {path.name}')
    return raw, raw.decode('utf-8')


def checked_file(root, name, expected):
    require(nonempty(name) and not Path(name).is_absolute(), 'Expected a relative file path')
    path = (root / name).resolve()
    require(path.is_relative_to(root), 'File path escapes audit directory')
    require(isinstance(expected, str) and re.fullmatch(r'[0-9a-f]{64}', expected), 'Invalid SHA256')
    raw, content = read_utf8(path)
    require(hashlib.sha256(raw).hexdigest() == expected, f'SHA256 mismatch: {name}')
    return content


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, f'Duplicate JSON key: {key}')
        out[key] = value
    return out


def audit(record_path):
    """Return a conservative report; stop at the first structural error."""
    try:
        record_path = Path(record_path).resolve()
        _, record_text = read_utf8(record_path)
        record = json.loads(record_text, object_pairs_hook=unique_object)
        require(isinstance(record, dict), 'Audit record must be an object')
        require(type(record.get('version')) is int and record['version'] == 1, 'Expected version 1')
        root = record_path.parent
        draft = checked_file(root, record.get('draft_file'), record.get('draft_sha256'))
        require(draft.strip(), 'Empty draft')
        require(not any(unicodedata.category(c) == 'Cf' for c in draft),
                'Invisible formatting character in draft; inspect before delivery')
        sources = record.get('sources')
        require(isinstance(sources, list), 'sources must be a list')
        source_texts = {}
        for source in sources:
            require(isinstance(source, dict), 'Source must be an object')
            sid = source.get('id')
            require(nonempty(sid) and sid not in source_texts, 'Missing or duplicate source id')
            require(source.get('kind') in ('provided', 'web'), 'Unknown source kind')
            require(nonempty(source.get('origin')), 'Source origin required')
            if source['kind'] == 'web':
                url = urlsplit(source['origin'])
                require(url.scheme in ('http', 'https') and url.hostname and not url.username and not url.password,
                        'Web origin must be an HTTP(S) URL without credentials')
                stamp = source.get('retrieved_at')
                require(nonempty(stamp), 'Web retrieval timestamp required')
                parsed = datetime.fromisoformat(stamp.replace('Z', '+00:00'))
                require(parsed.tzinfo is not None, 'Timestamp must include timezone')
            source_texts[sid] = checked_file(root, source.get('path'), source.get('sha256'))
        segments = record.get('segments')
        require(isinstance(segments, list) and segments, 'Nonempty segments list required')
        parts = []
        factual = 0
        for index, segment in enumerate(segments):
            require(isinstance(segment, dict), f'Segment {index} must be an object')
            body, kind = segment.get('text'), segment.get('kind')
            require(isinstance(body, str) and body, f'Segment {index} text is empty or invalid')
            require(isinstance(kind, str) and kind in KINDS, f'Segment {index} has unknown kind')
            evidence = segment.get('evidence', [])
            require(isinstance(evidence, list), f'Segment {index} evidence must be a list')
            if kind in ('fact', 'inference'):
                factual += 1
                require(body.strip() and evidence, f'Segment {index} needs evidence')
            for item in evidence:
                require(isinstance(item, dict), 'Evidence must be an object')
                sid, quote = item.get('source_id'), item.get('quote')
                require(isinstance(sid, str) and sid in source_texts, 'Unknown evidence source')
                require(nonempty(quote), 'Empty evidence quote')
                require(quote in source_texts[sid], f'Quote absent from source {sid}')
            parts.append(body)
        require(''.join(parts) == draft, 'Segments do not reproduce the entire final draft exactly')
        return {'status': PASS, 'draft_sha256': record['draft_sha256'],
                'segments': len(segments), 'fact_or_inference_segments': factual,
                'sources': len(source_texts),
                'limitations': ['Source retrieval and authenticity are not verified.',
                                'Claim classification, entailment, completeness, freshness and truth require semantic review.']}
    except (OSError, ValueError, TypeError, KeyError, UnicodeError, RecursionError) as error:
        return {'status': 'FAILED', 'error': str(error)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('audit_json', type=Path)
    args = parser.parse_args()
    result = audit(args.audit_json)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['status'] == PASS else 1


if __name__ == '__main__':
    raise SystemExit(main())
