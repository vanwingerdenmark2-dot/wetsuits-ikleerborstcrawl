#!/usr/bin/env bash
# wetsuit-preflight.sh — verplichte start-check vóór elke wijziging aan de wetsuits-site.
# Doel: in één commando de volledige staat tonen en afwijkingen flaggen, zodat je
# nooit werkt op een verouderde kopie of op een verkocht/gearchiveerd/spook-pak.
#
# Gebruik:   bash scripts/wetsuit-preflight.sh
# Exit-code: 0 = schoon, 1 = afwijkingen gevonden (los eerst op vóór je wijzigt).

set -euo pipefail
cd "$(dirname "$0")/.."   # repo-root, ongeacht waar je 'm aanroept

issues=0
flag() { echo "  ⚠️  $1"; issues=$((issues+1)); }

echo "═══════════════════════════════════════════════════════════"
echo " WETSUIT PRE-FLIGHT  ·  $(pwd)"
echo "═══════════════════════════════════════════════════════════"

# ── 1. Sync-status met live (origin/main) ──────────────────────
echo ""
echo "1) SYNC MET LIVE (origin/main)"
if git fetch origin --quiet 2>/dev/null; then
  behind=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo "?")
  ahead=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo "?")
  if [ "$behind" != "0" ]; then
    flag "Lokaal loopt $behind commit(s) ACHTER op live — eerst 'git pull' / ff-mergen vóór je wijzigt."
  else
    echo "  ✓ lokaal gelijk met live (achter: $behind, voor: $ahead)"
  fi
else
  echo "  (kon niet fetchen — offline? controleer handmatig)"
fi

# ── 2. Statussweep: detail vs overzicht vs archief ─────────────
echo ""
echo "2) STATUS PER PAK  (detail-status | in overzicht | bijzonderheden)"
printf "   %-40s %-13s %-12s\n" "PAK" "DETAIL" "OVERZICHT"
for dir in */; do
  d="${dir%/}"
  case "$d" in _archief|scripts|.git|.github) continue;; esac
  [ -f "${dir}index.html" ] || continue
  [ "$d" = "reparatie" ] && continue

  body=$(grep -o '<body class="[^"]*"' "${dir}index.html" | head -1 || true)
  case "$body" in
    *status-sold*)     st="VERKOCHT" ;;
    *status-reserved*) st="GERESERVEERD" ;;
    *)                 st="beschikbaar" ;;
  esac

  if grep -q "href=\"${d}/\"" index.html; then inov="ja"; else inov="NEE"; fi
  # status zoals die op de overzichtskaart staat
  cardstatus=$(grep -o "href=\"${d}/\" class=\"[^\"]*\"" index.html | grep -o 'status-sold\|status-reserved' || true)

  printf "   %-40s %-13s %-12s\n" "$d" "$st" "$inov"

  # Afwijkingen
  if [ "$inov" = "NEE" ] && [ "$st" = "beschikbaar" ]; then
    flag "$d: SPOOKPAGINA — niet in overzicht, niet gearchiveerd, geen status. Hoort die er nog te zijn?"
  fi
  if [ "$inov" = "ja" ]; then
    if [ "$st" = "VERKOCHT" ] && [ "$cardstatus" != "status-sold" ]; then
      flag "$d: detail=VERKOCHT maar overzichtskaart niet — statussen lopen niet synchroon."
    fi
    if [ "$st" = "GERESERVEERD" ] && [ "$cardstatus" != "status-reserved" ]; then
      flag "$d: detail=GERESERVEERD maar overzichtskaart niet — statussen lopen niet synchroon."
    fi
    if [ "$st" = "beschikbaar" ] && [ -n "$cardstatus" ]; then
      flag "$d: overzichtskaart heeft status ($cardstatus) maar detailpagina niet — niet synchroon."
    fi
  fi
done

# ── 3. Redirects wijzen naar bestaande pagina's ────────────────
echo ""
echo "3) REDIRECTS (netlify.toml)"
if [ -f netlify.toml ]; then
  while read -r target; do
    # alleen interne pad-redirects naar een pak-map controleren
    case "$target" in
      /*-*/) clean="${target#/}"; clean="${clean%/}"
        if [ ! -d "$clean" ]; then
          flag "Redirect wijst naar niet-bestaande map: $target"
        fi ;;
    esac
  done < <(grep -oE 'to = "[^"]*"' netlify.toml | sed 's/to = "//; s/"//')
  echo "  ✓ redirects gecontroleerd"
else
  echo "  (geen netlify.toml)"
fi

# ── Samenvatting ───────────────────────────────────────────────
echo ""
echo "═══════════════════════════════════════════════════════════"
if [ "$issues" -eq 0 ]; then
  echo " ✅ SCHOON — geen afwijkingen. Veilig om te wijzigen."
else
  echo " ⚠️  $issues AFWIJKING(EN) — eerst oplossen / met Mark afstemmen vóór je wijzigt."
fi
echo "═══════════════════════════════════════════════════════════"
[ "$issues" -eq 0 ]
