# Fretboard Card Generation Guide

## Context
Rey is learning guitar and wants Anki cards for fretboard memorization. The card system supports single notes, scales, arpeggios, and chord shapes rendered on an interactive SVG fretboard. See `FRETBOARD_CARD_DESIGN.md` for the technical card template design.

## Data Format
Tab-separated file. Fields: `Type`, `Name`, `Dots`, `Root`, `Notes`, `Shape`, `Key`, `Tags`

- `Type`: "note", "scale", "arpeggio", "chord"
- `Name`: human-readable name shown on card front
- `Dots`: comma-separated `string-fret` pairs (string 1=high E, 6=low E, fret 0=open)
- `Root`: the root dot position (e.g. `6-5` for A on low E string)
- `Notes`: comma-separated note names matching each dot
- `Shape`: position/shape identifier
- `Key`: the key (for color coding root vs other notes)
- `Tags`: space-separated Anki tags

## What to Generate

### 1. Single Notes (DONE — 78 cards)
Already generated in `fretboard_cards.txt`. Every string/fret combo, frets 0-12.

### 2. Essential Open Chords (~20 cards)
Common first-position chords every guitarist knows.

```
chord	C major	1-0,2-1,3-0,4-2,5-3	5-3	C,E,G,C,E	Open	C	Chords::Open
chord	A major	1-0,2-2,3-2,4-2,5-0	5-0	A,E,A,C#,E	Open	A	Chords::Open
chord	G major	1-3,2-3,3-0,4-0,5-2,6-3	6-3	G,B,D,G,B,G	Open	G	Chords::Open
chord	E major	1-0,2-0,3-1,4-2,5-2,6-0	6-0	E,B,E,G#,B,E	Open	E	Chords::Open
chord	D major	1-2,2-3,3-2,4-0	4-0	D,A,D,F#	Open	D	Chords::Open
chord	Am	1-0,2-1,3-2,4-2,5-0	5-0	A,E,A,C,E	Open	Am	Chords::Open
chord	Em	1-0,2-0,3-0,4-2,5-2,6-0	6-0	E,B,E,G,B,E	Open	Em	Chords::Open
chord	Dm	1-1,2-3,3-2,4-0	4-0	D,A,D,F	Open	Dm	Chords::Open
chord	C7	1-0,2-1,3-3,4-2,5-3	5-3	C,E,Bb,C,E	Open	C	Chords::Open
chord	A7	1-0,2-2,3-0,4-2,5-0	5-0	A,E,G,C#,E	Open	A	Chords::Open
chord	E7	1-0,2-0,3-1,4-0,5-2,6-0	6-0	E,B,E,G#,D,E	Open	E	Chords::Open
chord	D7	1-2,2-1,3-2,4-0	4-0	D,A,C,F#	Open	D	Chords::Open
chord	G7	1-1,2-0,3-0,4-0,5-2,6-3	6-3	G,B,D,G,B,F	Open	G	Chords::Open
chord	Fmaj (barre)	1-1,2-1,3-2,4-3,5-3,6-1	6-1	F,C,F,A,C,F	Barre E shape	F	Chords::Barre
chord	Bm (barre)	1-2,2-3,3-4,4-4,5-2,6-2	6-2	B,F#,B,D,F#,B	Barre Am shape	Bm	Chords::Barre
```

Generate all common open chords: C, G, D, A, E, Am, Em, Dm, F, Bm, plus 7th variants.

### 3. Barre Chord Shapes (~24 cards)
E-shape and A-shape barre chords in common keys. Major, minor, 7th, minor 7th.

Keys to cover: F, F#, G, Ab, A, Bb, B (E-shape barre)
Keys to cover: Bb, B, C, C#, D, Eb (A-shape barre)

For each: major, minor, 7, m7 = ~24-30 cards

### 4. CAGED System (~15 cards)
5 shapes × 3 keys = 15 cards. Show each CAGED shape for C, A, G, E, D forms.

```
chord	C major (C shape)	...dots...	...root...	C,E,G...	CAGED C	C	Chords::CAGED
chord	C major (A shape)	...dots...	...root...	C,E,G...	CAGED A	C	Chords::CAGED
chord	C major (G shape)	...dots...	...root...	C,E,G...	CAGED G	C	Chords::CAGED
chord	C major (E shape)	...dots...	...root...	C,E,G...	CAGED E	C	Chords::CAGED
chord	C major (D shape)	...dots...	...root...	C,E,G...	CAGED D	C	Chords::CAGED
```

### 5. Pentatonic Scale Shapes (~30 cards)
5 positions × major and minor × 3 keys = 30 cards

Keys: A minor, E minor, G major (most common guitar keys)

```
scale	Am pentatonic	6-5,6-8,5-5,5-7,4-5,4-7,3-5,3-7,2-5,2-8,1-5,1-8	6-5	A,C,D,E,G...	Position 1	Am	Scales::Pentatonic
scale	Am pentatonic	6-8,6-10,5-7,5-10,4-7,4-9...	6-8	C,D,E,G,A...	Position 2	Am	Scales::Pentatonic
```

### 6. Major Scale Shapes (~35 cards)
7 positions × 5 common keys = 35 cards

Keys: C, G, D, A, E

### 7. Essential Arpeggios (~48 cards)
For jazz, these are critical:

**Major arpeggios** (root, 3rd, 5th)
- All 5 CAGED positions × 4 common keys = 20 cards

**Minor arpeggios** (root, b3, 5th)
- 5 positions × 4 keys = 20 cards

**Dominant 7th arpeggios** (root, 3rd, 5th, b7)
- 5 positions × 4 keys = 20 cards

**Major 7th arpeggios** (root, 3rd, 5th, 7th)
- 5 positions × 4 keys = 20 cards

**Minor 7th arpeggios** (root, b3, 5th, b7)
- 5 positions × 4 keys = 20 cards

**Diminished arpeggios** (root, b3, b5)
- 3 positions × 3 keys = 9 cards

Keys to prioritize: C, G, A, D, E, F, Bb (jazz keys)

### 8. Jazz Chord Voicings (~40 cards)
Essential jazz voicings that every jazz guitarist should know:

**Shell voicings (Freddie Green style)**
- Root on 6th string: maj7, m7, dom7, m7b5
- Root on 5th string: maj7, m7, dom7, m7b5
- 8 voicings × 3 keys = 24 cards

**Drop 2 voicings**
- Root position, 1st inversion, 2nd inversion, 3rd inversion
- For maj7, m7, dom7
- String sets: 4321 and 5432
- ~24 cards

**Drop 3 voicings**
- Same inversions for maj7, m7, dom7
- String sets: 6321 and 5421
- ~24 cards

**Common jazz chords**
- 9th chords, 13th chords, altered dominants
- maj9, m9, 13, 7#9, 7b9, 7alt
- ~20 cards

### 9. Chord Inversions (~36 cards)
For each triad quality (major, minor, dim, aug):
- Root position, 1st inversion, 2nd inversion
- On string sets: 321, 432, 543
- 4 qualities × 3 inversions × 3 string sets = 36 cards

Keys: C, A, G

### 10. Common Jazz Progressions as Shapes (~20 cards)
ii-V-I voicings in different keys and positions:
- Show the shape of a full ii-V-I on the fretboard
- Multiple dots with different colors per chord
- "Play Dm7 → G7 → Cmaj7 in this position"

## Priority Order
1. ✅ Single notes (done)
2. Open chords (easiest wins, build confidence)
3. Barre chord shapes
4. Pentatonic scales (most useful for improvisation)
5. Major scale shapes
6. CAGED system
7. Major/minor arpeggios
8. 7th arpeggios
9. Jazz chord voicings (shell → drop 2 → drop 3)
10. Chord inversions
11. Jazz progressions as shapes

## Generation Notes
- All positions should be verified against actual guitar fretboard
- String numbering: 1 = high E (thinnest), 6 = low E (thickest)
- Fret 0 = open string
- Root notes should be clearly marked (different color in template)
- For scales/arpeggios, generate fingering-friendly positions (no impossible stretches)
- For jazz voicings, use standard voicing references (e.g. Ted Greene, Joe Pass)
- When generating inversions, ensure the bass note matches the inversion
- Tag hierarchy: Chords::Open, Chords::Barre, Chords::CAGED, Chords::Jazz, Scales::Pentatonic, Scales::Major, Arpeggios::Major, Arpeggios::Minor, Arpeggios::Dom7, etc.

## Approximate Total: ~350 cards
- 78 single notes
- 20 open chords
- 24 barre chords
- 15 CAGED
- 30 pentatonic
- 35 major scale
- 100 arpeggios
- 40 jazz voicings
- 36 inversions
- 20 jazz progressions

## File Output
Generate as tab-separated .txt files, one per category:
- `fretboard_notes.txt` (done)
- `fretboard_open_chords.txt`
- `fretboard_barre_chords.txt`
- `fretboard_caged.txt`
- `fretboard_pentatonic.txt`
- `fretboard_major_scales.txt`
- `fretboard_arpeggios.txt`
- `fretboard_jazz_voicings.txt`
- `fretboard_inversions.txt`
- `fretboard_jazz_progressions.txt`

Or one combined file: `fretboard_all_cards.txt`
