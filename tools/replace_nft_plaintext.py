#!/usr/bin/env python3
import re
from pathlib import Path

# Case-preserving replacement helper
REPLIES = {
    'lower': 'arts',
    'title': 'Arts',
    'upper': 'ARTS',
}

word_re_plural = re.compile(r"\bnfts\b", re.IGNORECASE)
word_re = re.compile(r"\bnft\b", re.IGNORECASE)
html_tag_re = re.compile(r"(<[^>]+>)")
template_re = re.compile(r"(\{\{.*?\}\}|\{%.*?%\})", re.DOTALL)


def replace_case_preserving(match: re.Match) -> str:
    text = match.group(0)
    if text.isupper():
        return REPLIES['upper']
    if text[0].isupper():
        return REPLIES['title']
    return REPLIES['lower']


def transform_plain_text(content: str) -> str:
    # Split content into HTML tags and non-tag text
    parts = re.split(html_tag_re, content)
    out = []
    for part in parts:
        if not part:
            continue
        # If it's an HTML tag, keep as-is
        if part.startswith('<') and part.endswith('>'):
            out.append(part)
            continue
        # For non-tag text, further split by template blocks and process only plain text
        subparts = re.split(template_re, part)
        for sub in subparts:
            if not sub:
                continue
            if template_re.fullmatch(sub):
                # Inside Django/Jinja template syntax – skip
                out.append(sub)
            else:
                # Plain text – replace 'nfts' and 'nft' with 'arts' (case-preserving)
                replaced = word_re_plural.sub(replace_case_preserving, sub)
                replaced = word_re.sub(replace_case_preserving, replaced)
                # Replace specific brand terms
                replaced = replaced.replace('RareFinds', 'Rare Vault')
                replaced = replaced.replace('Rare Finds', 'Rare Vault')
                out.append(replaced)
    return ''.join(out)


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding='utf-8')
    new = transform_plain_text(raw)
    if new != raw:
        path.write_text(new, encoding='utf-8')
        return True
    return False


def main():
    root = Path(__file__).resolve().parents[1]
    templates_dir = root / 'templates'
    if not templates_dir.exists():
        print(f"No templates directory at: {templates_dir}")
        return

    html_files = list(templates_dir.rglob('*.html'))
    changed = []
    for f in html_files:
        if process_file(f):
            changed.append(f.relative_to(root).as_posix())

    print(f"Processed {len(html_files)} .html files.")
    print(f"Updated {len(changed)} files.")
    for p in changed[:20]:
        print(f" - {p}")
    if len(changed) > 20:
        print(f" ... and {len(changed) - 20} more")


if __name__ == '__main__':
    main()
