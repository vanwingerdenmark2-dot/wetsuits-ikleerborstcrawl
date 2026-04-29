# Wetsuits IkLeerBorstcrawl

Statische website voor 2dehands wetsuits van IkLeerBorstcrawl.nl.

## Live op
`https://wetsuits.ikleerborstcrawl.nl/`

## Structuur
```
/
├── index.html                                       # overzichtspagina
├── netlify.toml                                     # Netlify config + redirects
├── deboer-fjord-3-0-series-2-heren-l/
│   ├── index.html
│   └── fotos/
├── dare2tri-mach3-fm-dames-m/
│   ├── index.html
│   └── fotos/
└── roka-maverick-mx-gen1-dames-m/
    ├── index.html
    └── fotos/
```

## Deploy
- GitHub repo → Netlify auto-deploy bij elke push naar `main`
- DNS: CNAME `wetsuits` → Netlify-app op DNS van Hostnet (ikleerborstcrawl.nl)

## Wetsuits in catalogus

| Slug | Pak | Prijs |
|---|---|---|
| `deboer-fjord-3-0-series-2-heren-l` | deboer Fjord 3.0 Series 2 — Heren maat L | € 549 |
| `dare2tri-mach3-fm-dames-m` | Dare 2 Tri Mach 3 FM — Dames maat M | € 169 |
| `roka-maverick-mx-gen1-dames-m` | ROKA Maverick MX Gen.I — Dames maat M | € 269 |

## Korte URL's (redirects)
- `/deboer` → deboer Fjord
- `/mach3` → Dare 2 Tri Mach 3 FM
- `/roka` → ROKA Maverick MX

## Maintenance
Voor updates aan een wetsuit: pas de bijbehorende `index.html` aan en commit. Netlify deployt automatisch binnen 30-60 sec.

Voor een nieuwe wetsuit:
1. Maak nieuwe map met slug-naam (bv. `merk-model-geslacht-maat`)
2. Plaats `index.html` (kopie van bestaande, content aangepast)
3. Plaats `fotos/` submap met alle gerefereerde afbeeldingen
4. Voeg link toe in root `index.html` (overzichtspagina)
5. Commit + push
