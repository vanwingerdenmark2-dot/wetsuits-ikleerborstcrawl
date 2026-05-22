#!/usr/bin/env python3
"""Archiveert verkochte wetsuits ouder dan 3 weken uit de overzichtspagina."""

import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
INDEX_HTML = REPO_ROOT / "index.html"
NETLIFY_TOML = REPO_ROOT / "netlify.toml"
ARCHIEF_DIR = REPO_ROOT / "_archief"
DREMPEL_DAGEN = 21


def te_archiveren_wetsuits(html: str, vandaag) -> list:
    grens = vandaag - timedelta(days=DREMPEL_DAGEN)
    resultaat = []
    for m in re.finditer(r'<a\s[^>]*data-status-label="VERKOCHT"[^>]*>', html):
        tag = m.group(0)
        href = re.search(r'href="([^/"]+)/"', tag)
        datum = re.search(r'data-verkocht-datum="(\d{4}-\d{2}-\d{2})"', tag)
        if href and datum:
            verkocht_op = datetime.strptime(datum.group(1), "%Y-%m-%d").date()
            if verkocht_op <= grens:
                resultaat.append(href.group(1))
    return resultaat


def verwijder_kaart(html: str, folder: str) -> str:
    patroon = (
        r'\n[ \t]*(?:<!--[^\n]*-->\n[ \t]*)?'
        rf'<a\s[^>]*href="{re.escape(folder)}/"[^>]*>.*?</a>'
    )
    return re.sub(patroon, '', html, flags=re.DOTALL)


def voeg_redirect_toe(toml: str, folder: str) -> str:
    if f'from = "/{folder}' in toml:
        return toml
    redirect = f'\n[[redirects]]\n  from = "/{folder}/*"\n  to = "/"\n  status = 301\n'
    return toml.replace('[[headers]]', redirect + '[[headers]]')


def main():
    vandaag = datetime.now().date()
    html = INDEX_HTML.read_text(encoding="utf-8")

    folders = te_archiveren_wetsuits(html, vandaag)
    if not folders:
        print("Geen wetsuits te archiveren vandaag.")
        return

    ARCHIEF_DIR.mkdir(exist_ok=True)
    toml = NETLIFY_TOML.read_text(encoding="utf-8")

    for folder in folders:
        print(f"Archiveren: {folder}")
        html = verwijder_kaart(html, folder)
        toml = voeg_redirect_toe(toml, folder)
        src = REPO_ROOT / folder
        if src.exists():
            shutil.move(str(src), str(ARCHIEF_DIR / folder))

    INDEX_HTML.write_text(html, encoding="utf-8")
    NETLIFY_TOML.write_text(toml, encoding="utf-8")
    print(f"Klaar — {len(folders)} wetsuit(s) gearchiveerd.")


if __name__ == "__main__":
    main()
