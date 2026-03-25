# Music Anki Cards

Interactive Anki flashcard system for learning guitar fretboard, sheet music reading, piano keys, and ear training.

## Card Types

| Deck | Cards | Description |
|------|-------|-------------|
| **Fretboard** | 265 | Notes, scales, chords, triads, arpeggios with interval labels |
| **Sheet Music** | 29 | Treble + bass clef note reading |
| **Piano** | 97 | Notes, chords, scales |
| **Ear Training** | 52 | Interval recognition from guitar roots |
| **Total** | **443** | |

Each note type generates two card types from the same data:
- **Recognition** — see the visual, identify/name it
- **Recall** — see the name, reproduce the visual by tapping

## Features

- Interactive SVG fretboard/staff/piano with tap-to-play audio
- 12-note chromatic color system for visual note identification
- Interval labels on dots (1, b3, 5, b7, etc.)
- Ghost hover indicators for recall mode
- Dark mode support (Anki Desktop, AnkiMobile, AnkiDroid)
- Card maker with AnkiConnect integration

## Structure

```
templates/          Anki card templates (front/back HTML)
  fretboard/        Guitar fretboard cards
  sheet-music/      Staff notation cards
  piano/            Piano keyboard cards
  ear-training/     Interval ear training cards
styles/             Shared CSS stylesheets
data/               Tab-separated card data files
previews/           Browser preview & tools
  card_browser.html Browse all cards with front/back preview
  card_maker.html   Create new guitar cards with AnkiConnect
  *_preview.html    Standalone previews per instrument
docs/               Design docs and guides
scripts/            Data generation scripts
```

## Quick Start

1. Serve the folder: `python3 -m http.server 8090`
2. Open `http://localhost:8090/previews/card_browser.html`
3. To create cards: open `http://localhost:8090/previews/card_maker.html`

## Importing to Anki

1. Create note types in Anki matching the template fields
2. Copy template HTML into Anki's card template editor
3. Copy CSS into the styling section
4. Import `.txt` data files as tab-separated

## Design System

See `docs/ANKI_DESIGN_SYSTEM.md` for the full design system documentation, reusable across any domain.
