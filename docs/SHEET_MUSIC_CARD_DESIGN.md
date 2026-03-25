# Sheet Music Card System Design

## Note Type: Sheet Music
### Fields:
- `Type` — "note", "chord", "interval"
- `Name` — "B4", "Cmaj7", "minor 3rd"
- `Clef` — "treble", "bass"
- `KeySig` — "C", "G", "Bb", "F#" (key signature — determines sharps/flats on staff)
- `TimeSig` — "4/4", "3/4" (optional, for context display)
- `Notes` — staff positions: "B4" or "B4,D#5,F#5" (for chords)
- `Accidentals` — per-note overrides: "sharp,none,sharp" (when note has accidental not in key sig)

### Card Types:

#### Card 1: Recognition
- Front: Shows notehead(s) on staff with clef + key signature, "What note is this?"
- Back: Note name revealed with color-coded answer section
- Tap the note to hear it

#### Card 2: Recall
- Front: Staff with clef + key signature + note name, "Place this note on the staff"
- User taps a staff line/space to place the notehead
- Back: Shows correct position (green/red/dashed overlay)

### SVG Staff Rendering
- 5 lines, 4 spaces
- Ledger lines as needed (up to 2 above/below)
- Clef symbol (treble/bass)
- Key signature (sharps/flats)
- Time signature (optional)
- Noteheads: filled oval on line or space
- Accidentals next to notehead when needed

### Staff Position Encoding
- Notes encoded as pitch + octave: C4, D#5, Bb3
- Treble clef: bottom line = E4, top line = F5
- Bass clef: bottom line = G2, top line = A3
- Positions mapped to Y coordinates on the SVG

### Note Range
- Treble clef: C4 (middle C, 1 ledger below) to G5 (2 ledgers above)
- Bass clef: B1 (2 ledgers below) to D4 (1 ledger above middle C)
- Single notes first, chords later

### Audio
- Same Web Audio API synth as fretboard (shared frequency math)
- MIDI note numbers: C4=60, D4=62, E4=64, F4=65, G4=67, A4=69, B4=71

### Note Color System
Same palette as fretboard cards (by pitch class, ignoring octave).

### Styling
- Same card aesthetic (Nunito, light/dark mode, CSS variables)
- Tag: 🎼 Sheet Music
- Answer section: color-coded by note, pulse animation, clickable to play
