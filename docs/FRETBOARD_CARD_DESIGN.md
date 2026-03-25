# Fretboard Card System Design

## Status: Built
All templates, CSS, data, and preview are complete.

### Card Counts (204 entries = ~408 Anki cards)
- 78 fretboard single notes
- 10 pentatonic scales (Am + Em, 5 positions each)
- 3 blues boxes (BB King, Albert King, SRV)
- 10 scales (C major 5 positions + A minor 5 positions)
- 48 triads (6 keys × major/minor × 4 string sets)
- 14 chords (10 open + 4 barre)
- 20 arpeggios (8 jazz + 12 dominant 7th in all keys)
- 21 ii-V-I patterns (7 common jazz keys × 3 chords each)

All entries include Intervals field for color-coded interval display.

## Files
- `fretboard_card_style.css` — Anki card CSS (light/dark, animations, colors)
- `fretboard_front1.html` — Card 1 front (Recognition)
- `fretboard_back1.html` — Card 1 back (Recognition)
- `fretboard_front2.html` — Card 2 front (Recall)
- `fretboard_back2.html` — Card 2 back (Recall)
- `fretboard_preview.html` — Interactive preview (both modes, audio, dark mode)
- `fretboard_cards.txt` — Data file (78 single-note cards)

## Note Type: Fretboard
### Fields:
- `Type` — "note", "scale", "arpeggio", "chord"
- `Name` — "Am pentatonic", "Cmaj7 arpeggio", "G barre chord", "A"
- `Dots` — encoded positions: `6-5,5-5,5-7,4-5,4-7,3-5` (string-fret pairs, order matters for scales/arpeggios)
- `Root` — which dot is the root: `6-5`
- `Notes` — note names: `A,D,E,G,A,D`
- `Shape` — "Position 1", "CAGED E shape", etc.
- `Key` — for color coding

### Card Types:

#### Card 1: Recognition
- Front: Shows dots on fretboard, "What is this?"
- Back: Shows the name + notes labeled on dots
- Tap anywhere on fretboard to hear that position's note
- Answer section is color-coded by note (same palette as key cards)
- Note name has pulse animation on reveal (keyPulse)
- Entire answer area is clickable to play the note

#### Card 2: Recall
- Front: Blank fretboard + name (e.g. "A major arpeggio, 1st inversion")
- User taps fretboard to place dots (tap again to remove — no undo/clear buttons)
- Back: Overlays correct answer on fretboard
  - Green: correct positions
  - Red: wrong positions
  - Dashed outline: missing positions
- Answer section shows note name with same color coding
- For scales/arpeggios (Type field): dots are numbered to show order
- For chords: dots are plain (order doesn't matter)

### Order Matters Logic (TODO — not yet implemented)
- Controlled by `Type` field
- `scale` or `arpeggio` → placed dots get small numbered circles, back checks position AND order
- `chord` or `note` → plain dots, back only checks positions
- Order comes from comma-separated sequence in `Dots` field

### Single Note Cards (78 total)
- Type: "note"
- Dots: single position like "6-5"
- Name: note name like "A"
- 6 strings × 13 frets (0-12)
- Front: fretboard with pulsing dot, "What note is this?"
- Back: note name revealed, dot shows note label

### Audio
- Web Audio API synth — triangle wave + soft harmonic overtone
- MIDI note calculated from string tuning + fret
- freq = 440 * 2^((midi-69)/12)
- Tuning: E4(64), B3(59), G3(55), D3(50), A2(45), E2(40)
- Tap any fretboard position to hear it (tap zones rendered on top of dots in SVG z-order)

### SVG Fretboard Rendering
- 12 frets, 6 strings
- Nut, fret wires, dot markers (3,5,7,9, double at 12)
- String thickness increases low to high
- String labels on left, fret numbers below
- Tap zones cover all 78 positions (always present for audio)
- Uses CSS variables for light/dark mode
- Responsive width (max 540px)

### Note Color System
Each note gets a unique background color on the answer section (matches key card colors):
```
C: #DC4040 (red)       C#: #6A1FCC (violet)
D: #E8C820 (yellow)    D#: #9898A0 (gray)
E: #6AADBD (teal)      F:  #9B1B1B (dark red)
F#: #7B2DB8 (purple)   G:  #E08030 (orange)
G#: #B85EB0 (pink)     A:  #2E8B57 (green)
A#: #A85A30 (brown)    B:  #4169E1 (blue)
```
Text color auto-adjusts (light/dark) based on background luminance.

### Styling
- Nunito font
- Tag: 🎸 Fretboard
- Answer section: color-coded background, hover brightens (filter: brightness(1.1))
- "tap to play" hint text at bottom of answer area
- Night mode via CSS variables (`.night_mode` and `.nightMode`)
- keyPulse animation on note reveal

### Data File
- `fretboard_cards.txt` — tab-separated: String, Fret, Note, Tags
- 78 cards for single notes
- TODO: Add scale/arpeggio/chord entries with multi-dot Dots field

### Preview
- `fretboard_preview.html`
- Mode tabs: Recognition / Recall
- Controls: String, Fret, Show, Random, Dark Mode, Show Back
- Full audio playback on tap
- Both card types rendered side by side when Show Back is checked

---

## TODO / Next Steps for Fretboard
1. Implement numbered dots for scales/arpeggios (order-matters logic based on Type field)
2. Add scale data entries (pentatonic shapes, major/minor positions)
3. Add arpeggio data entries (major, minor, dominant 7th shapes)
4. Add chord data entries (open chords, barre chords, CAGED shapes)
5. Consider a card maker tool for easier data entry
