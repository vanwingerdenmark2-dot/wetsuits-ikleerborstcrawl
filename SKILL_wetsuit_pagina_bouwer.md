---
name: wetsuit-pagina-bouwer
description: Bouw of corrigeer een productpagina voor de 2dehands wetsuits-website van IkLeerBorstcrawl. Trigger bij elke vraag over: nieuwe wetsuit-pagina maken, bestaande pagina aanpassen, foto's verwerken, prijzen of klasse aanpassen, conditie-update. Geldig voor `/wetsuits-site-build/<slug>/index.html` en de overzichts-`index.html`.
type: skill
laatst_bijgewerkt: 2026-04-30
---

# Wetsuit-pagina-bouwer

> **Status:** Single Source of Truth voor élke wetsuit-pagina op de 2dehands-site. Vandaag, morgen, over 10 jaar. Geldt voor Cowork én Claude Code.
>
> **Ondergeschikt aan:** MARK_PRIME.md (gedrag/tone). Aanvullend voor: tech-specifieke uitwerking van wetsuit-productpagina's.

---

## 0. Eén ijzeren wet — verkopen, niet ondermijnen

**Het doel van elke pagina is een wetsuit te verkopen of verhuren. Punt.**

Niet: ons indekken. Niet: alle slechte dingen breeduit melden. Niet: elke twijfel op de pagina dumpen.

Drie stelregels van Mark, woord voor woord:

1. **"Iets wat je niet weet, komt er niet bij."** Geen "onbekend", geen "niet beschikbaar online", geen "vraag via WhatsApp" om een gat te vullen. Gewoon weglaten.
2. **"Goede dingen zet je erop. Slechte dingen laat je weg zonder te lachen."** Klinkt cynisch, is gewoon hoe verkoop werkt.
3. **"De klasse-aanduiding zegt al wat de koper mag verwachten."** Klasse B = max 1-2 kleine reparaties. Daar hoef je niet bij te schrijven dat dit pak één scheurtje van 1,5 cm heeft. De klasse-uitleg op de pagina zelf doet dat werk al.

Concreet: vermeld een specifieke conditie-issue **maximaal één keer** en alleen in het conditie-blok. Verstop het niet, maar maak er geen marketing-thema van.

---

## 1. Pagina-structuur (vaste h2-volgorde)

Elke detail-pagina volgt **exact** deze sectie-volgorde, ongeacht het pak:

1. **Hero** — foto-carousel + info-card (titel, badges, prijs + huidig-model-prijs, WhatsApp-CTA, verhuur-tabel + borg). **Geen** apart maattabel-blok hier.
2. **Over dit pak** — 1 alinea, maximaal 2 alinea's. Wat is het, voor wie. Geen pseudo-features.
3. **Voor wie is dit pak?** — 4-punts profielblok (Niveau / Pasvorm / Type zwemmer / Sterkste punt voor jou) + disclaimer **met de maattabel-link**.
4. **Speciale features van de [merk] [model]** — vaste sectie, **niet optioneel**. Tech-grid (2x2) met 4 features, elk met titel, kort sub-line en uitleg. Foto's hergebruikt uit de carousel-set (4 van de 6 promo-foto's). Verboden: features verzinnen — alleen feitelijke, geverifieerde technologie uit de research-bron. Als er niet genoeg feitelijke tech is voor 4 cards: bouw er 3 of 2, maar niet minder. Alle andere pagina's volgen dit patroon — zonder deze sectie valt een pagina visueel uit de toon.
5. **Conditie** — kort. Klasse + maximaal 1-2 li's als er iets specifieks te melden valt.
6. **Wat betekent "tweedehands"?** — generieke uitleg drie klassen (zelfde tekst op elke pagina; alleen de actieve klasse-card verschilt). **Direct na Conditie**, zodat klasse en uitleg naast elkaar staan.
7. **Specs** — alleen wat we 100% weten. Onbekende velden weg. **Geen** "Conditie-klasse"-rij hier (al in Conditie-blok).
8. **Garantie en restitutie** — generiek (vaste tekst).
9. **Vragen?** — WhatsApp-CTA herhaling.

**Volgorde-rationale:** koper leest top-down: pak → voor wie → conditie ("Middenklasse B") → wat betekent dat? → specs (alle technische data) → garantie. Conditie en de uitleg ervan staan naast elkaar, niet gescheiden door een specs-blok.

---

## 2. Hero-blok — wat erop, wat eraf

### Badges (max 3, boven de prijs)

- **Klasse-badge** (verplicht): "Topstaat (A)" / "Middenklasse (B)" / "Voordeelklasse (C)" — `class="badge gold"`
- **Maximaal 2 extra positieve badges** zoals "IRONMAN-approved", "Vrijwel nieuw", "Niet meer beschikbaar bij merk", "Ouder model" — kies wat verkoopt
- **NOOIT op badge-niveau:**
  - "Reparatie inbegrepen" — staat al in conditie-info
  - "Anderszins prima staat" — onnodige geruststelling, ondermijnt
  - "Geen reparaties" / "Geen beschadigingen" — zegt iets te veel
  - Verwijzingen naar specifieke schade

### Prijs

- **Verkoopprijs** prominent (`class="now"`) in zwart/donker
- **Doorgehaalde prijs** met label, save-percentage, structuur:

  ```html
  <div class="price-koop">
    <span class="now">€&nbsp;X</span>
    <span class="was-label">[LABEL]</span>
    <span class="was">€&nbsp;Y</span>
    <span class="save">−Z%</span>
  </div>
  ```

  Het label is verplicht — anders snapt de koper niet wat het doorgehaalde getal betekent.

- **CSS-layout** (verplicht): de prijs (`.now`) staat op een **eigen regel groot**, label + doorgehaalde + save-badge op de **regel daaronder netjes uitgelijnd**:

  ```css
  .price-koop {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px 12px;
    margin-bottom: 8px;
  }
  .price-koop .now {
    width: 100%;            /* forceert eigen regel */
    font-size: 40px;
    font-weight: 700;
    color: #1a2942;
    line-height: 1;
    margin-bottom: 4px;
  }
  .price-koop .was-label { font-size: 13px; color: #6b7d97; }
  .price-koop .was { text-decoration: line-through; color: #8e9bb1; font-size: 16px; }
  .price-koop .save { background: #fff2c2; color: #8a5a05; font-size: 12px; font-weight: 700; padding: 3px 8px; border-radius: 4px; }
  ```

  Niet alles op één rij smijten — dat oogt rommelig.

- **Twee labels** afhankelijk van situatie:

  - **`Nieuwprijs`** — als de doorgehaalde prijs de officiële nieuwprijs (adviesprijs) is van **dit specifieke model**. Voorwaarde: het pak is nog in productie of er is een betrouwbare officiële MSRP-bron.
  - **`Huidig model`** — als de doorgehaalde prijs van een **opvolger** is, niet van dit pak zelf (dit pak is een oudere variant). Plus een korte uitleg in de extras-line eronder: `Huidig model = [opvolger] bij [merk]`.

- **Save-percentage** alleen tonen als de korting duidelijk groter is dan ~30% (anders leest het als irritant). Berekening: `(was − now) / was × 100`, afronden naar geheel getal.

- **Geen Engelse jargon-termen** zoals "MSRP", "RRP", "SRP" op de pagina. Gebruik altijd Nederlandse termen: "Nieuwprijs" / "Officiële nieuwprijs" / "Adviesprijs". MSRP staat ook NIET in spec-grid labels.

- **Extras-line eronder** voor extra context (bv "Huidig model = …" of merk-info). Klein, 12px, grijs (`#6b7d97`).

### WhatsApp-CTA

Vaste opzet:
```html
<a class="cta" href="https://wa.me/31641891443?text=Hoi%2C%20ik%20heb%20interesse%20in%20de%20[MERK]%20[MODEL]%20[GENDER]%20maat%20[MAAT]%20-%20kun%20je%20me%20meer%20vertellen%3F">
```

CTA-tekst: **"Stuur me een berichtje op WhatsApp"**. Niet: "Vraag foto's van het werkelijke pak" of vergelijkbaar — dat suggereert dat de pagina onvolledig is.

### Verkoopprijs bepalen — Marktplaats-onderkant

**Regel:** als Mark de verkoopprijs niet zelf opgeeft, bepaal je hem door op **Marktplaats (en vergelijkbare 2dehands-platforms zoals Vinted)** te kijken naar:
- hetzelfde merk + model
- vergelijkbaar productiejaar (max 1-2 jaar verschil)
- vergelijkbare conditieklasse (A/B/C)

Daarna prijs je het pak in op **de onderkant van die markt** — vergelijkbaar met de laagste aanbieding, of net daaronder als de conditie identiek is. Reden: dit blijft een 2dehands-shop voor IkLeerBorstcrawl-klanten, niet een premium-tweedehands-platform. Snelle doorloop is belangrijker dan maximaal rendement per pak.

Bij twijfel of geen vergelijkbare aanbiedingen: stel een prijs voor en vraag Mark om bevestiging in plaats van te gokken op een te hoog bedrag.

### Verhuurtabel + borg

Standaard 4 verhuur-tarieven (1 dag / weekend / midweek / week).

**Hoe je de bedragen bepaalt (verplicht) — gekoppeld aan de verkoopprijs, NIET aan de klasse.** De conditieklasse (A/B/C) zegt niets over de huurprijs — een goedkoop en een duur pak van dezelfde klasse huren níét voor hetzelfde bedrag. De waarde van het pak (= de verkoopprijs) bepaalt de huur.

1. **Dagtarief naar verkoopprijs:**

   | Verkoopprijs | Dagtarief |
   |---|---|
   | < € 80 | € 10 |
   | € 80 – 149 | € 15 |
   | € 150 – 249 | € 20 |
   | € 250 + | € 25 |

2. **Vaste ladder vanaf het dagtarief:** weekend = 2× · midweek = 3× · hele week = 4×.
   - Dagtarief € 10 → € 10 / 20 / 30 / 40
   - Dagtarief € 15 → € 15 / 30 / 45 / 60
   - Dagtarief € 20 → € 20 / 40 / 60 / 80
   - Dagtarief € 25 → € 25 / 50 / 75 / 100

Wijzigt de verkoopprijs (bv. een pak zakt een klasse en wordt goedkoper)? Dan loopt de huur automatisch mee via de band — niet los bepalen.

**Afrondingsregel — verplicht:** alle verhuurbedragen worden afgerond op **€5**. Geen € 18, € 23, € 38 of € 67 — altijd € 20, € 25, € 40, € 65 of € 70. Dit geldt voor zowel de verhuurtabel op de detail-pagina als de "vanaf €X / dag"-regel op de homepage-kaart en de "huur het pak eerst (€X / dag)"-regel in de Voor-wie-disclaimer. Reden: nette ronde bedragen ogen professioneler en zijn makkelijker te onthouden.

Na de tabel **altijd** dit borg-blokje:

```html
<div style="margin-top: 10px; padding: 10px 12px; background: #f6f9fc; border-radius: 6px; font-size: 12px; color: #4a5a76; line-height: 1.5;">
  <strong style="color: #1a2942;">Borg:</strong> € 100 bij verhuur. Bij ongeschonden inlevering volledig terug — kleine nagelscheurtjes (≤ 10 cent-stuk) zijn geen probleem, dat is gewoon gebruik. Bij grotere scheuren worden reparatiekosten volgens onze <a href="../reparatie/" style="color: #0a6cb1;">reparatie-tarieven</a> van de borg ingehouden.
</div>
```

### Maattabel-link

**NIET** in een apart blok in de hero. **WEL** geïntegreerd in de Voor-wie-disclaimer (zie sectie 4). Daar past hij logisch: koper kijkt eerst naar pasvorm-profiel, dan naar maattabel ter verificatie.

---

## 3. "Over dit pak" — kort, positief, feitelijk

Maximaal 2 alinea's. Schrijven wat het pak IS en VOOR WIE.

**Niet:** alle features herhalen die straks in de specs komen.
**Niet:** "het pak verkeert in vrijwel nieuwe staat" — daar is de Conditie-sectie voor.
**Niet:** uitleggen wat we niet weten.

Foto-disclaimer (als er geen foto's van het werkelijke pak zijn): max 1 zin in kleine tekst onderin de sectie:

```html
<p style="font-size: 13px; color: #6b7d97;">Foto's tonen de [MERK] [MODEL]-lijn — vergelijkbaar met dit pak.</p>
```

**Geen alarm-kaders boven de foto's.** Geen `.photo-alert`-blok, geen "Let op!"-overlays. Foto's, prijs en CTA krijgen de aandacht — nooit een disclaimer.

---

## 4. "Voor wie is dit pak?" — 4-punts profiel

Vaste structuur, identiek op élke pagina (alleen content verschilt):

```
- Niveau: [recreatief / age-grouper / wedstrijd / instap]
- Pasvorm: [maat + officiële maattabel-link]
- Type zwemmer: [welke lichaamsbouw / zwemstijl past het]
- Sterkste punt voor jou: [waarom dit specifieke pak voor dit profiel goed is]
```

Disclaimer onderaan (vaste structuur, **maattabel-link inbegrepen**):
```html
<div class="profiel-disclaimer">
  <strong>Twijfel je over de maat?</strong> Dit is een richtlijn — geen absolute regel. Bekijk de officiële <a href="[MERK MAATTABEL URL]" target="_blank" rel="noopener">[merk] maattabel</a>, of huur het pak eerst (€&nbsp;X / dag) om te ontdekken of het écht bij je past.
</div>
```

CSS-classes: `.profiel-grid`, `.profiel-card`, `.profiel-label`, `.profiel-text`, `.profiel-disclaimer`. Klakkeloos hergebruiken op elke pagina.

---

## 5. Conditie-blok — minimaal

**Default-regel (verplicht):** alleen de klasse-aanduiding. Verder NIETS. De klasse-uitleg verderop op de pagina vertelt al wat de koper mag verwachten — daar hoeft het conditie-blok niet aan toe te voegen.

```html
<ul>
  <li><strong>Conditie-klasse: [Topstaat (A) / Middenklasse (B) / Voordeelklasse (C)]</strong></li>
</ul>
```

**Een tweede regel komt er ALLEEN bij als Mark dat expliciet aangeeft.** Niet uit eigen interpretatie, niet uit research, niet uit ChatGPT-chats (die kunnen verouderd zijn — Mark heeft het pak fysiek in handen, alleen zijn actuele oordeel telt). Als Mark zegt *"er zit ook een badmuts en handschoentjes bij"* of *"ik heb het zelf 2x getest"*, dán komt er een tweede `<li>`. Anders niet.

**Wat NOOIT in het conditie-blok:**
- **Specifieke beschrijving van schade** ("3 scheurtjes, 2 op de borst en 1 op de schouder", "scheurtje van 1,5 cm", "lichte slijtage in de oksels"). Wekt onnodig wantrouwen. De klasse zegt alles. **Alleen als Mark expliciet vraagt om een specifieke schade-vermelding, neem je het over — woord voor woord zoals hij het formuleert.**
- "Geen andere scheuren / geen rits-schade / geen overige reparaties" → wekt verdenking dat er meer is.
- Lange uitleg over reparatie-procedure — staat op de aparte reparatiepagina.
- Schade-info uit ChatGPT-chats of andere research-bronnen overnemen. Die data is een momentopname die op het moment van publicatie achterhaald kan zijn (Mark heeft het pak in tussentijd misschien meer gebruikt). **Alléén Mark's actuele instructie is bron voor schade-beschrijving.**

---

## 6. Specs-blok — alleen wat we weten

**Conditie-klasse staat NIET in Specs** — alleen in het Conditie-blok hierboven. Dubbele vermelding voorkomen.

**Verplichte velden** (vul alleen in als verifieerbaar):
- Merk (verplicht)
- Model (verplicht)
- Type (verplicht)
- Maat + maattabel-link (verplicht)

**Optionele velden** (alleen als zeker bekend):
- Kleur
- Gewicht (officiële merk-spec)
- Neopreen-dikte / buoyancy-profiel
- Speciale features (alleen patented/geverifieerde)
- Wedstrijdgoedkeuring
- Generatie / SKU
- Oorspronkelijke nieuwprijs (officiële MSRP)

**Verboden:**
- "Onbekend", "Niet meer beschikbaar online", "Vraag via WhatsApp", "Specificaties oudere variant niet beschikbaar"
- Een veld met `.value.unknown` class — verwijderen, niet labelen
- Gokwerk over neopreen-dikte, technologie, gewicht of nieuwprijs

**Regel:** kun je een veld niet verifiëren? Verwijder de hele rij. Korte specs > brede specs met gaten.

---

## 7. Foto's — werkelijk vooraan, promotioneel daarna

### Aantal: kwaliteit boven kwantiteit

**4-5 foto's die kloppen** > 8 foto's waarvan er een paar niet eens lijken op het aangeboden pak. Een carousel met mismatchende foto's wekt twijfel; weinig sterke foto's verkopen beter.

**Regel:** elke foto in de carousel moet **redelijk lijken op het aangeboden pak** (kleurstelling, panelen-indeling, model). Lijkt een foto er niet op? Verwijderen — niet "ter referentie" laten staan.

### Volgorde in carousel — STRIKT (één bron, geen mengelmoes)

**De foto's die Mark per pagina aanlevert (typisch 6 stuks in een submap "NIEUWE FOTOS-nog hernoemen") = de hele carousel. Geen werkelijke foto's er nog bijzetten als die er ook zijn. Geen oude promo-foto's er nog bijzetten. Geen mengelmoes.**

Reden: alle wetsuits-pagina's moeten visueel identiek opgebouwd zijn (6 foto-thumbs, dezelfde sfeer). Mengelmoes zorgt dat één pagina opvalt — bijvoorbeeld doordat de hoofdfoto een leeg pak op een hangertje is terwijl alle andere pagina's een persoon op het strand tonen. Dat is precies wat een koper voelt als "die ene pagina klopt niet".

**Regels:**
1. **Hoofdfoto (`<img id="mainImage">`) en eerste thumb = vooraanzicht uit de aangeleverde set.** Bij naamgeving zoals `[slug]-promo-front-A.jpg`.
2. **Carousel-volgorde:** vooraanzicht → driekwart rechts → achteraanzicht → driekwart links → sfeerbeeld (zittend/staand) → vooraanzicht-variant. Of een vergelijkbare logische sequentie afhankelijk van wat er beschikbaar is.
3. **Counter:** `1 / [aantal aangeleverde foto's]`. Niet meer, niet minder.
4. **Homepage-thumb (kaart op `index.html`):** zelfde eerste foto als de hoofdfoto van de detail-pagina. Een kaart toont nooit een ander beeld dan waar je op terechtkomt.

**Verboden:**
- Werkelijke pakfoto's (telefoonfoto's, advertentie-foto's) bij de aangeleverde set zetten "voor extra context". De koper kan ze altijd alsnog bekijken via WhatsApp.
- Officiële merkfoto's van internet halen om de carousel te "vullen".
- AI-promo's mengen met werkelijke foto's in dezelfde carousel.
- Aparte "Werkelijk pak"-sectie maken naast de carousel.

**Wat als er nog WEL eerder werkelijke foto's op disk staan?** Niet in de carousel zetten. Niet linken. Eventueel verwijderen uit de fotos-map (alleen na akkoord van Mark — zie sectie 3.1 MARK_PRIME geen workarounds zonder overleg).

### Disclaimer onderaan (canonieke tekst — één variant, geen uitzonderingen)

Het credits-blok onderaan **élke** wetsuit-pagina bevat exact deze ene zin, woord-voor-woord. Geen bronnenlijst, geen URL-verwijzingen, geen "© [merk]", geen "eerste foto's / overige foto's"-uitleg. Eén tekst, identiek op alle pagina's:

```html
<div class="credits">
  <strong>Disclaimer:</strong> Promotionele foto's vergelijkbaar met het aangeboden pak. Kleurstellingen en details kunnen iets afwijken van het wetsuit dat wij te koop aanbieden op deze pagina.
</div>
```

**Waarom één tekst, ook als er werkelijke pakfoto's bij staan?** Omdat de pagina's allemaal op dezelfde manier zijn opgebouwd en consistente formuleringen vertrouwen wekken. Wisselende disclaimer-formuleringen tussen pagina's wekken juist de indruk dat er iets achter wordt gehouden.

**Geen bronvermelding (URL-lijst, fotograaf, persfoto-link).** Niet nodig, leidt af, en wekt schijn van juridische zorg waar koper geen behoefte aan heeft.

### Bestandsnamen

- Werkelijk pak: `[merk]-werkelijk-front.jpg`, `[merk]-werkelijk-back.jpg`, `[merk]-werkelijk-detail-[X].jpg`
- Officiële merkfoto's: behoud bestaande naamgeving van het merk (bv. `roka-mx-buoyancy-detail.jpg`)
- AI-renders / promotionele indicatieve foto's: gebruik beschrijvende namen met merk-prefix (bv. `d2t-mach3-fm-voorkant.jpg`). Niet "render" of "ai" in filename — Mark beschouwt promotionele foto's gelijk aan officiële merkbeelden.

### Foto-disclaimer

Eén canonieke disclaimer onderaan élke pagina (zie sectie hierboven). Geen aparte foto-disclaimer in de hero, geen alarm-blok bovenaan, geen overlay op de foto. De canonieke disclaimer onderin volstaat.

### Geen Engelse handelstermen

**Verboden in alle zichtbare tekst (specs, prijs-blok, badges, conditie-tekst):**
- `RRP` (Recommended Retail Price) → gebruik **adviesprijs**
- `MSRP` (Manufacturer's Suggested Retail Price) → gebruik **adviesprijs**
- `SRP` (Suggested Retail Price) → gebruik **adviesprijs**
- `Sold Out` → gebruik **uitverkocht** of **niet meer leverbaar**
- `Exclusive` (in product-context) → gebruik **exclusief** of laat weg

Reden: dit is een Nederlandstalige consumentensite, geen retail-vakblad. Engelse handelstermen sluiten kopers uit die het jargon niet kennen, en passen niet bij de toon van de rest van de site. Vaktermen die wél internationaal gangbaar zijn voor het product zelf (zoals "neopreen", "buoyancy", "Yamamoto", model-namen) blijven natuurlijk staan — die hebben geen Nederlandse vertaling die beter werkt.

**Specifieke acties als je deze termen tegenkomt in research-bronnen:** vertaal naar Nederlands, niet letterlijk overnemen.

### HEIC-conversie

Foto's komen vaak binnen als `.HEIC`. Convert met:
```bash
convert "Originele/foto.HEIC" -auto-orient -resize 1600x1600\> -quality 88 "doel/naam.jpg"
```

Plaats de originelen niet in de fotos-root maar in een submap (bv. `Originele fotos/` of `fotos eigen wetsuit/`). De geconverteerde JPGs staan in de fotos-root en worden door de pagina gebruikt.

---

## 8. Tone & woordkeuze

- **Direct en feitelijk.** Geen marketingtaal als "geweldig", "uniek", "perfect".
- **Positief framen.** "€ 269 voor een pak van € 640 nieuw" — niet "het pak is goedkoop omdat het 2dehands is".
- **Korte zinnen.** Maximaal 25 woorden per zin in productbeschrijvingen.
- **Geen herhalingen.** Een feit één keer noemen, niet 3 keer.
- **Geen disclaimer-taal.** "Mits", "indien", "uitgezonderd" — vermijden tenzij juridisch nodig.

---

## 9. Anti-patronen — NOOIT doen

Gebaseerd op concrete fouten uit de bouw van de eerste 4 pagina's:

1. ❌ **Een groot opvallend kader (alarm-blok) boven de foto's** met disclaimer over het pak. Dat is het eerste wat de koper ziet en het ondermijnt direct.
2. ❌ **Specifieke schade-beschrijving op de pagina zetten** (badges, conditie-blok, "Voor wie", disclaimer of waar dan ook) zonder dat Mark daar expliciet om vroeg. De klasse-aanduiding (A/B/C) en de generieke klasse-uitleg in "Wat betekent tweedehands?" doen het werk. Schade-details uit een ChatGPT-research, oude Vinted-advertentie of eigen interpretatie van foto's mogen NIET overgenomen worden. Alléén Mark's eigen actuele woorden zijn bron — en alleen als hij expliciet zegt *"zet erbij dat..."*.
3. ❌ **"Specificaties niet beschikbaar online — vraag via WhatsApp"** als spec-veld. Veld verwijderen, niet vullen.
4. ❌ **"Geen andere scheuren, geen rits-schade, geen overige reparaties"** als conditie-claim. Roept de vraag op of er nog meer is. Klasse B vertelt dit al impliciet.
5. ❌ **CTA-tekst "Vraag foto's van het werkelijke pak"** in plaats van standaard "Stuur me een berichtje". Suggereert dat de pagina onvolledig is.
6. ❌ **`.value.unknown`** spec-velden met "Onbekend voor deze variant". Veld weghalen.
7. ❌ **Foto-overlay-warn** badges op de mainfoto ("Voorbeeldfoto Mach 3-lijn"). Foto laten praten, geen overlay.
8. ❌ **Officiële merkfoto's of AI-promo's anders behandelen** dan elkaar. Beide zijn promotioneel materiaal — gelijk framen.
9. ❌ **Lange "Over de foto's"-alinea midden in de productbeschrijving.** Maximaal 1 zinnetje, 13px grijs.
10. ❌ **Aannemen wat een vorige sessie heeft achtergelaten.** Bij twijfel over de huidige staat: lees de pagina, verifieer voor je verandert.
11. ❌ **Sleutelfeiten verzinnen** (nieuwprijs, neopreen-dikte, generatie). Bij onzekerheid: verwijderen of overslaan, niet gokken. Zie MARK_PRIME 3.3 Regel A.
12. ❌ **Foto's plaatsen die niet (echt) lijken op het aangeboden pak** "ter referentie". Liever 4 die kloppen dan 8 met mismatchende ruis ertussen.
13. ❌ **Foto-bronnenlijst onderaan** met URL-verwijzingen naar persfoto's, merk-galleries of Marktplaats-credits. Eén korte disclaimer-zin is genoeg.
14. ❌ **Conditie-klasse twee keer noemen** (in Conditie-blok én als rij in Specs-grid). Dubbele info — alleen in Conditie-blok.
15. ❌ **Apart "Twijfel je over de maat?"-blok in de hero**. Maattabel-link hoort in de Voor-wie-disclaimer, niet als losstaand kader bij de prijs.
16. ❌ **Specs-velden met "ca." of "schat" voor onbekende waarden** (gewicht, neopreen-dikte). Bij twijfel hele rij weghalen.
17. ❌ **Sectie-volgorde Specs vóór Wat-betekent-tweedehands**. Conditie en de uitleg daarvan moeten naast elkaar staan, met Specs daarna.
18. ❌ **Breadcrumb met alleen "Home › [pak]"** (2-niveaus). Altijd 3 niveaus, met klikbare gender-categorie ertussen.
19. ❌ **Doorgehaalde prijs zonder label** (`<span class="was">€ 640</span>` zonder `was-label` ervoor). Koper weet dan niet of dat een eerdere vraagprijs of een nieuwprijs is. Altijd met label "Nieuwprijs" of "Huidig model".
20. ❌ **Engelse jargon-termen op de pagina**: "MSRP", "RRP", "SRP", "USD", "OEM". Gebruik Nederlands: "Nieuwprijs", "Officiële nieuwprijs", "Adviesprijs". Engels jargon wekt afstand en verwarring.
21. ❌ **Eigen eerdere vraagprijs als doorgehaalde was-prijs**. Doorgehaald getal = altijd officiële nieuwprijs van dit model OF van het huidige opvolger-model. Eigen prijscorrecties horen niet als "korting" getoond te worden.

---

## 10. Klasse-uitleg (vaste generieke tekst — kopiëren tussen pagina's)

Elke pagina bevat dezelfde "Wat betekent tweedehands?"-sectie. Alleen de **actieve klasse-card** verschilt per pak:

```html
<div class="klasse-card active">  <!-- alleen op actieve klasse -->
  <span class="klasse-letter">B</span>
  <div class="klasse-name">Middenklasse</div>
  <div class="klasse-desc">Maximaal 1 of 2 kleine, professioneel uitgevoerde reparaties...</div>
</div>
```

De andere twee `<div class="klasse-card">` (zonder `active`).

**Niet aanpassen:** de descriptie-tekst van de drie klassen is generiek en gelijk op elke pagina. Niet aan zitten.

---

## 11. Borg-regel + reparatie-tarieven (vaste tekst)

Op elke pagina, onder de verhuurtabel:

```
Borg: € 100 bij verhuur. Bij ongeschonden inlevering volledig terug — kleine nagelscheurtjes (≤ 10 cent-stuk) zijn geen probleem, dat is gewoon gebruik. Bij grotere scheuren worden reparatiekosten volgens onze [reparatie-tarieven](../reparatie/) van de borg ingehouden.
```

Niet aanpassen. Niet inkorten. Linkt altijd naar `../reparatie/`.

---

## 12. Overzichts-pagina (`wetsuits-site-build/index.html`) — kaart per pak + filter

### Filter-balk bovenaan
4 knoppen: **Alle wetsuits / Heren / Dames / Kinder**. Klikken filtert kaarten via JS, URL-hash update naar `#heren-wetsuits` / `#dames-wetsuits` / `#kinder-wetsuits`. Bij lege categorie verschijnt empty-state ("Op dit moment zijn er geen … wetsuits beschikbaar"). De filter-bar staat **boven** de grid, **onder** de intro.

### Kaarten — data-categorie attribuut verplicht
Elke kaart heeft:
```html
<a href="..." class="card" data-categorie="heren|dames|kinder" style="...">
```

Zonder `data-categorie` werkt het filter niet voor die kaart.

### Kaart-velden:
- **Foto:** liefst de werkelijke voorkant van het pak (of de mooiste promo-foto)
- **Brand + model**
- **Meta:** "[Gender] · Maat [X] · [type/positie]"
- **Badges:** klasse + max 1 verkoop-positieve (NOOIT meer)
- **Prijs:** now + eventueel was (doorgehaald)
- **Verhuur-vanaf-prijs**
- **CTA:** "Bekijk dit pak"

### JS-script onderaan (vaste tekst)
Verplicht: het filter-script aan het eind van de body, vóór `</body>`. Leest hash bij laden, koppelt klikken aan filter-state, zorgt dat directe links uit detailpagina's (`../index.html#dames-wetsuits`) automatisch het juiste filter activeren.

## 12b. Breadcrumb (op detailpagina's én reparatiepagina)

3-niveaus, eerste twee klikbaar:

```html
<div class="crumbs">
  <a href="../index.html">Home</a>
  &nbsp;›&nbsp; <a href="../index.html#[gender]-wetsuits">[Gender] wetsuits</a>
  &nbsp;›&nbsp; [Volledige naam — Gender maat X]
</div>
```

Waarbij `[gender]` één van: `heren`, `dames`, `kinder`. Het derde niveau (pak-naam) is **geen link** — dat is de huidige pagina.

Op de reparatiepagina:
```html
<div class="crumbs">
  <a href="../index.html">Home</a>
  &nbsp;›&nbsp; Reparatieservice
</div>
```

(Geen tussen-niveau, want reparatie is geen wetsuit-categorie.)

---

## 13. Verifieer-checklist (afronden voor publiceren)

Vóór een pagina als klaar wordt gemarkeerd, deze 8 punten doorlopen:

- [ ] Geen `.photo-alert` of `photo-overlay-warn` in HTML
- [ ] Geen `.value.unknown` spec-velden
- [ ] Geen "vraag via WhatsApp" als invulling van een spec-veld
- [ ] Geen "Geen reparaties / Geen beschadigingen / Geen andere scheuren" badges of bullets
- [ ] Conditie-blok: alleen klasse + maximaal 1 specifieke regel, niet meer
- [ ] Foto-disclaimer is óf weg óf 1 zin in kleine grijze tekst
- [ ] Alle gerefereerde foto-paths bestaan (run grep + ls)
- [ ] Counter klopt met aantal thumbnails
- [ ] Borg-tekst klopt met de standaard
- [ ] Klasse-badge in hero komt overeen met `klasse-card active` in de tweedehands-uitleg
- [ ] WhatsApp-CTA tekst is "Stuur me een berichtje op WhatsApp"
- [ ] Overzichts-pagina kaart is ook bijgewerkt (en heeft `data-categorie` attribuut!)
- [ ] Elke foto in de carousel lijkt redelijk op het aangeboden pak — geen mismatchende ruis
- [ ] Credits-blok bevat alleen 1 korte disclaimer-zin met `<strong>Disclaimer:</strong>`-prefix, geen bronnenlijst
- [ ] Sectie-volgorde: Conditie → Wat betekent tweedehands → Specs (NIET Specs → Tweedehands)
- [ ] Specs-grid bevat **geen** "Conditie-klasse"-rij (al in Conditie-blok)
- [ ] Maattabel-link staat in de Voor-wie-disclaimer, NIET als apart blok in de hero
- [ ] Breadcrumb is 3-niveaus diep, eerste twee klikbaar
- [ ] Extras-line onder de prijs vermeldt "Huidige model: ca. € X" (alleen als prijs zeker is)
- [ ] Doorgehaalde prijs heeft een label ("Nieuwprijs" of "Huidig model") — anders niet plaatsen
- [ ] Geen Engelse jargon ("MSRP", "RRP", "SRP", "USD") op de pagina
- [ ] Alle verhuurbedragen afgerond op € 5 (zowel verhuurtabel, homepage-kaart `vanaf €X` als Voor-wie-disclaimer)
- [ ] Verhuur-dagtarief past bij de verkoopprijs-band (sectie 2) en de ladder = 2× / 3× / 4× (weekend / midweek / week)

---

## 14. Bestandsstructuur

```
wetsuits-site-build/
├── index.html                          # Overzichts-pagina
├── reparatie/
│   └── index.html                      # Reparatieservice + tarieven
├── [slug]/
│   ├── index.html                      # Detail-pagina
│   └── fotos/
│       ├── [merk]-werkelijk-*.jpg      # Foto's werkelijk pak (eerst in carousel)
│       ├── [merk]-[andere].jpg         # Officiële/promo-foto's (daarna)
│       └── Originele fotos/            # HEIC-originelen (niet in carousel)
└── SKILL_wetsuit_pagina_bouwer.md      # Dit document
```

Slug-conventie: `[merk]-[model-kort]-[gender]-[maat]`. Voorbeelden:
- `deboer-fjord-3-0-series-2-heren-l`
- `roka-maverick-mx-gen2-dames-m`
- `dare2tri-mach3-fm-dames-m`
- `zone3-vision-dames-m`

**Meerdere identieke pakken (zelfde merk + model + gender + maat):** Mark heeft soms meerdere exemplaren van hetzelfde pak. Dan komt er een uniek-makende suffix achter de slug:

- 1e exemplaar: `[merk]-[model]-[gender]-[maat]` (geen suffix)
- 2e exemplaar: `...-2`
- 3e exemplaar: `...-3`
- enzovoort

Eventueel mag Mark ook een omschrijvende suffix kiezen als de exemplaren echt verschillen op een zichtbaar kenmerk (bv. `-zwart` vs `-blauw`, of `-klasse-c` als de klasses van de twee exemplaren verschillen). De suffix komt dan in plaats van het volgnummer.

**Op de detail-pagina én homepage-kaart:** zorg dat beide identieke pakken visueel onderscheidbaar zijn. Bij meerdere exemplaren van zelfde merk/model:
- voeg in de h2 of de meta-regel een onderscheidend kenmerk toe (bv. "#2", de conditieklasse, of de zichtbare kleur),
- of laat het verschil zien via badges (bv. één heeft "Topstaat (A)" en de ander "Middenklasse (B)").

Doel: een koper die op de homepage scrollt moet direct snappen dat dit twee verschillende exemplaren zijn, niet een dubbele kaart.

Bij naam-/modelcorrectie: slug hernoemen via `mv`, niet via duplicate. QR-codes pas drukken nadat de slug definitief is.

---

## Changelog

- **2026-04-30** — Initieel opgesteld door Cowork na expliciete instructie van Mark om alle lessen uit de bouw van de eerste 4 wetsuit-pagina's vast te leggen. Aanleiding: herhaaldelijke fouten op de Mach 3 FM-pagina (te veel scheurtje-vermeldingen, "vraag via WhatsApp"-spec-velden, alarm-blok boven foto's).
- **2026-04-30** — Sectie 7 uitgebreid met foto-keuze-regel (4-5 goede > 8 met mismatchende ruis) en credits-blok-versimpeling (alleen 1 korte disclaimer-zin, geen bronnenlijst). Anti-patronen 12 en 13 toegevoegd.
- **2026-04-30** — Major update: sectie-volgorde gewijzigd (Conditie → Tweedehands-uitleg → Specs), conditie-klasse niet meer in Specs-grid, maattabel-link verplaatst naar Voor-wie-disclaimer, breadcrumb naar 3-niveaus met categorie-tussenniveau, prijs-blok uitgebreid met huidig-model-prijs in extras-line, credits-blok krijgt "**Disclaimer:**"-prefix, homepage uitgebreid met filter-balk (Alle/Heren/Dames/Kinder) + JS-koppeling met URL-hash. Anti-patronen 14-18 toegevoegd, verifieer-checklist met 5 punten uitgebreid.
- **2026-04-30** — Prijs-blok: doorgehaalde prijs verplicht met label ("Nieuwprijs" voor dit specifieke model, "Huidig model" voor opvolger). Geen Engels jargon meer (MSRP/RRP/SRP). Anti-patronen 19-21 toegevoegd, verifieer-checklist met 2 extra punten. Aanleiding: Mach 3 FM toonde verwarrende €169 als doorgehaalde prijs (eigen eerdere vraagprijs, geen MSRP) en op andere pagina's stond "MSRP" als jargon.
- **2026-04-30** — Disclaimer onderaan teruggebracht naar **één canonieke tekst** ("Promotionele foto's vergelijkbaar met het aangeboden pak..."), geen versie A/B-onderscheid meer. Aanleiding: Mark merkte op dat de disclaimer-tekst tussen pagina's afweek. Pagina's zijn op identieke manier opgebouwd dus de disclaimer hoort identiek te zijn — wisselende formuleringen wekken wantrouwen. Tegelijk: homepage-sortering toegevoegd (4 opties, default prijs hoog→laag) en filter-knoppen verlengd naar "Heren wetsuits / Dames wetsuits / Kinder wetsuits". Sort-bar als compacte rechts-uitgelijnde dropdown.
- **2026-04-30** — **Major skill-fix**: foto-regel herschreven naar "alléén de aangeleverde set in de carousel, geen werkelijke pak-foto's en officiële merk-foto's mengen". Aanleiding: Fjord 3.0 had eerder mengelmoes (5 werkelijke + 4 officiële) en Mark voegde 6 nieuwe AI-promo's toe. Cowork interpreteerde de skill-regel "Hoofdfoto = altijd eerste werkelijke pakfoto" als bevel om die mengelmoes te behouden, met als resultaat dat Fjord opviel ten opzichte van de andere 9 pagina's (op homepage werd Fjord-thumb een leeg pak op hangertje terwijl alle andere kaarten een AI-promo met persoon op strand tonen). Mark belangrijk citaat: *"Wat is hier anders aan dan alle andere wetsuits die we tot nog toe hebben gedaan? Waarom doe jij nou in één keer anders?"* Skill-regel was de bron van de fout. Tegelijk: nieuwe sectie "Geen Engelse handelstermen" toegevoegd (RRP/MSRP/SRP/Sold Out → adviesprijs/uitverkocht), en RRP-vermeldingen op DHB Hydron, HUUB Archimedes II en ROKA Gen.I weggehaald.
- **2026-05-01** — Sectie 5 (Conditie-blok) herschreven naar default "alleen klasse-aanduiding, niets meer". Tweede `<li>` mag uitsluitend op expliciete instructie van Mark — niet uit ChatGPT-research, oude Vinted-advertentie of eigen interpretatie. Anti-patroon 2 herschreven: specifieke schade-beschrijving (bv. "3 scheurtjes, 2 op borst, 1 op schouder") is **verboden** tenzij Mark er woord-voor-woord om vraagt. Aanleiding: Orca Alpha Heren M kreeg een conditie-li met scheurtjes-detail uit een chat van enkele dagen oud, terwijl Mark expliciet had aangegeven dat de schade inmiddels groter was (vandaar klasse C) maar dat hij die zelf niet wilde uitspecificeren. Citaat: *"Ik heb inmiddels al veel meer scheurtjes erbij; vandaar ook voor de klasse C. Maar jij mag niet zomaar overnemen en beschrijven wat er precies wel of niet is."* ChatGPT-chats zijn momentopnames; alleen Mark's actuele oordeel telt voor schade-info.
- **2026-05-01** — Verhuurprijs-afrondingsregel toegevoegd aan sectie 2 en verifieer-checklist: alle verhuurbedragen worden afgerond op €5 (geen €18, €23, €38 — altijd €20, €25, €40 etc.). Geldt voor verhuurtabel, homepage-kaart "vanaf €X" en Voor-wie-disclaimer. Aanleiding: Orca Alpha kreeg verhuurprijzen €18 / €38 / €55 / €70 die Mark allemaal omhoog wilde naar het volgende veelvoud van 5. Tegelijk Zone3 Vision verhuur-tabel en homepage-kaart gefixt (€18 → €20 op alle 3 plekken).
- **2026-06-16** — **Verhuurprijs-bepaling gecodificeerd** (sectie 2 + checklist). Tot nu toe zei de skill alleen "4 tarieven, afronden op € 5" maar niet hóé je het bedrag bepaalt — in de praktijk volgde de huur losjes de verkoopprijs, inconsistent, en de interne ladder (weekend/midweek/week) verschilde per pagina (2,5×–4,6×). Nu vastgelegd: dagtarief via verkoopprijs-banden (<€80 → €10, €80–149 → €15, €150–249 → €20, €250+ → €25), vaste ladder 2× / 3× / 4×. Expliciet: huur is gekoppeld aan verkoopprijs, NIET aan klasse (bewijs: klasse A loopt van dhb Hydron €79=€10/dag tot deboer Fjord €549=€25/dag). Aanleiding: Mark vroeg of de verhuurprijzen per klasse waren vastgelegd of aan de verkoopprijs gekoppeld — bleek nergens geregeld. NB: enkele bestaande pagina's (o.a. Orca Alpha, BlueSeventy Helix, ROKA Gen.I/II) wijken nog af van de nieuwe banden en moeten nog worden bijgesteld.
- **2026-05-01** — Twee nieuwe regels toegevoegd: (1) **Verkoopprijs bepalen** (sectie 2) — als Mark geen verkoopprijs opgeeft, kijk op Marktplaats/Vinted naar zelfde merk + model + jaar + conditie en pak de onderkant van die markt. Snelle doorloop > maximaal rendement. (2) **Meerdere identieke pakken** (sectie 14) — slug krijgt suffix `-2`, `-3` etc., of een omschrijvende suffix (`-zwart`). Op de homepage-kaart moeten dubbele pakken visueel onderscheidbaar zijn via h2/meta/badges. Aanleiding: Mark kondigde aan dat hij regelmatig meerdere exemplaren van hetzelfde merk/model/maat heeft, en wil dat het systeem schaalbaar werkt voor 5+ identieke pakken zonder slug-conflicten.
