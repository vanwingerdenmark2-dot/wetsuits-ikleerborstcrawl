#!/usr/bin/env python3
"""
Voegt status-CSS en status-banner toe aan detailpagina's die dit nog missen.
Eenmalig uit te voeren — daarna niet meer nodig.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

STATUS_CSS = """
    .status-banner { display: none; }
    .page-status .status-banner {
      display: block; padding: 16px 20px; text-align: center;
      font-weight: 700; font-size: 15px; letter-spacing: 0.04em;
      color: #fff; text-shadow: 0 1px 2px rgba(0,0,0,0.25);
      box-shadow: 0 4px 14px rgba(0,0,0,0.18), 0 1px 0 rgba(255,255,255,0.2) inset;
    }
    .page-status .status-banner .sub {
      display: block; font-weight: 500; font-size: 13px;
      margin-top: 4px; letter-spacing: 0; opacity: 0.95;
    }
    .page-status.status-reserved .status-banner {
      background: linear-gradient(180deg, #fbbf24 0%, #d97706 55%, #92400e 100%);
    }
    .page-status.status-sold .status-banner {
      background: linear-gradient(180deg, #ef4444 0%, #b91c1c 55%, #7f1d1d 100%);
    }
    .page-status .rent-table { position: relative; opacity: 0.5; }
    .page-status .rent-table::after {
      content: "Verhuur niet beschikbaar zolang dit pak gereserveerd is";
      position: absolute; inset: 0; display: flex; align-items: center;
      justify-content: center; background: rgba(255,255,255,0.85);
      font-weight: 600; font-size: 13px; color: #4a5a76;
      text-align: center; padding: 0 12px;
    }
    .page-status.status-sold .rent-table::after {
      content: "Verhuur niet beschikbaar — dit pak is verkocht";
    }"""

STATUS_BANNER = """
  <div class="status-banner">
    Dit pak is op dit moment gereserveerd
    <span class="sub">Een andere klant is bezig dit pak te passen. Laat je naam achter voor de wachtlijst — als de reservering niet doorgaat krijg jij eerste kans.</span>
  </div>"""

SKIP = {"_archief", "reparatie", "scripts", ".github", ".git"}


def heeft_status_css(html: str) -> bool:
    return "status-banner" in html or "page-status" in html


def voeg_toe(folder: Path) -> bool:
    detail = folder / "index.html"
    if not detail.exists():
        return False

    html = detail.read_text(encoding="utf-8")

    if heeft_status_css(html):
        return False

    # CSS toevoegen voor </style>
    html = html.replace("  </style>", STATUS_CSS + "\n  </style>", 1)

    # Banner div toevoegen na <body> (ongeacht of er al een class op staat)
    html = re.sub(r'(<body[^>]*>)', r'\1' + STATUS_BANNER, html, count=1)

    detail.write_text(html, encoding="utf-8")
    print(f"Bijgewerkt: {folder.name}")
    return True


def main():
    bijgewerkt = 0
    for folder in sorted(REPO_ROOT.iterdir()):
        if folder.is_dir() and folder.name not in SKIP and not folder.name.startswith("."):
            if voeg_toe(folder):
                bijgewerkt += 1

    print(f"\nKlaar — {bijgewerkt} pagina('s) bijgewerkt.")


if __name__ == "__main__":
    main()
