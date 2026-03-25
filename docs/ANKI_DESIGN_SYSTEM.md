# Anki Design System

A domain-agnostic design system extracted from the music Anki cards (Fretboard, Sheet Music, Piano, Chord Progressions). These patterns, colors, animations, and conventions can be applied to any future card domain -- geography, chemistry, anatomy, language, math, or anything else.

---

## 1. Color System

### Light Mode Foundation

```css
.card {
  background: #FFFAF0;
  color: #333;
  --accent: #4ba9c8;
  --accent-text: #fff;
  --green: #3a9a5a;
  --red: #c75050;
  --text-primary: #333;
  --text-secondary: rgba(0,0,0,0.45);
  --bg-subtle: rgba(0,0,0,0.06);
  --bg-chip: rgba(0,0,0,0.12);
  --border-dashed: rgba(0,0,0,0.12);
}
```

### Dark Mode Foundation

```css
/* Desktop Anki + AnkiMobile */
.night_mode.card, .night_mode .card {
  background: #333b45;
  color: #e6e6e6;
  --accent: #4ba9c8;
  --accent-text: #1a2530;
  --green: #5db87a;
  --red: #c75a5a;
  --text-primary: #e6e6e6;
  --text-secondary: rgba(255,255,255,0.45);
  --bg-subtle: rgba(255,255,255,0.08);
  --bg-chip: rgba(255,255,255,0.15);
  --border-dashed: rgba(255,255,255,0.15);
}

/* AnkiDroid (different class name, same values) */
.nightMode.card, .nightMode .card {
  /* identical to .night_mode block above */
  background: #333b45;
  color: #e6e6e6;
  --accent: #4ba9c8;
  --accent-text: #1a2530;
  --green: #5db87a;
  --red: #c75a5a;
  --text-primary: #e6e6e6;
  --text-secondary: rgba(255,255,255,0.45);
  --bg-subtle: rgba(255,255,255,0.08);
  --bg-chip: rgba(255,255,255,0.15);
  --border-dashed: rgba(255,255,255,0.15);
}
```

**Key rule:** Both `.night_mode` (desktop/AnkiMobile) and `.nightMode` (AnkiDroid) selectors must always be included. They are identical in values but differ in class name casing.

### CSS Custom Properties Reference

| Variable | Light | Dark | Purpose |
|----------|-------|------|---------|
| `--accent` | `#4ba9c8` | `#4ba9c8` | Primary interactive color (same both modes) |
| `--accent-text` | `#fff` | `#1a2530` | Text on accent backgrounds |
| `--green` | `#3a9a5a` | `#5db87a` | Correct answers |
| `--red` | `#c75050` | `#c75a5a` | Wrong answers |
| `--text-primary` | `#333` | `#e6e6e6` | Main body text |
| `--text-secondary` | `rgba(0,0,0,0.45)` | `rgba(255,255,255,0.45)` | Labels, hints, metadata |
| `--bg-subtle` | `rgba(0,0,0,0.06)` | `rgba(255,255,255,0.08)` | Section backgrounds, tag bg |
| `--bg-chip` | `rgba(0,0,0,0.12)` | `rgba(255,255,255,0.15)` | Hover state, interactive chips |
| `--border-dashed` | `rgba(0,0,0,0.12)` | `rgba(255,255,255,0.15)` | Button borders, dividers |

### Domain-Specific Variables

Each card domain may add its own variables to the same `.card` block. Examples from existing domains:

```css
/* Fretboard / Sheet Music */
--fret-wire: rgba(0,0,0,0.3);     /* dark: rgba(255,255,255,0.2) */
--string-color: rgba(0,0,0,0.3);  /* dark: rgba(255,255,255,0.3) */
--staff-line: rgba(0,0,0,0.35);   /* dark: rgba(255,255,255,0.3) */
--staff-text: rgba(0,0,0,0.5);    /* dark: rgba(255,255,255,0.45) */

/* Chord Progressions */
--c-bor: #c87a08;    /* borrowed chords — dark: #f59e0b */
--c-dom: #7c3aed;    /* dominant function — dark: #a78bfa */
--c-ext: #2563eb;    /* extended chords — dark: #60a5fa */
--c-chr: #dc2626;    /* chromatic chords — dark: #f87171 */
--strike: #c75050;   /* strikethrough — dark: #ff6b6b */
```

### Note/Key Color Mapping (12-Color Chromatic Palette)

Used for color-coding answer sections by musical key. Generalizable to any domain with 8-16 categorical items.

| Item | Hex | Description |
|------|-----|-------------|
| C | `#DC4040` | Red |
| C# / Db | `#6A1FCC` | Violet |
| D | `#E8C820` | Yellow |
| D# / Eb | `#9898A0` | Gray |
| E | `#6AADBD` | Teal |
| F | `#9B1B1B` | Dark red |
| F# / Gb | `#7B2DB8` | Purple |
| G | `#E08030` | Orange |
| G# / Ab | `#B85EB0` | Pink |
| A | `#2E8B57` | Green |
| A# / Bb | `#A85A30` | Brown |
| B | `#4169E1` | Blue |

### Adaptive Text on Colored Backgrounds

When placing text on a color-coded background, use this luminance check to decide between light and dark text:

```javascript
function needsDarkText(hex) {
  var r = parseInt(hex.slice(1,3), 16);
  var g = parseInt(hex.slice(3,5), 16);
  var b = parseInt(hex.slice(5,7), 16);
  return (0.299 * r + 0.587 * g + 0.114 * b) > 160;
}
// true  -> use dark text:  rgba(0,0,0,0.7)
// false -> use light text: #fff
```

### Interval / Functional Role Colors

For elements that have a functional role relative to a root (scale degrees, grammatical parts, hierarchy levels):

| Role | Color | Use |
|------|-------|-----|
| Root / Primary | `var(--accent)` #4ba9c8 | The main reference point |
| Third / Secondary | `#e8a030` (warm) | Distinguishing quality |
| Fifth / Tertiary | `#5a8abf` (cool) | Supporting element |
| Seventh / Quaternary | `#9b59b6` (purple) | Extension/tension |
| Correct | `var(--green)` | Right answer overlay |
| Wrong | `var(--red)` | Wrong answer overlay |
| Missing | `var(--red)` dashed | Expected but not given |

---

## 2. Typography

### Font Stack

```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

.card {
  font-family: Nunito, -apple-system, 'Segoe UI', sans-serif;
  font-size: 22px;
  -webkit-text-size-adjust: 100%;
}
```

### Japanese Fallback (when needed)

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@500&display=swap');
@font-face { font-family: 'Yu Mincho'; src: url('_yumin.ttf'); }

.tag, .song-title {
  font-family: 'Yu Mincho', 'Noto Serif JP', serif;
}
```

### Size Scale

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Tag badge | 16-20px | 400 | Smaller for music, 20px for vocab |
| Prompt / Question label | 14px | 400 | `var(--text-secondary)` |
| Name / Title | 24px | 700 | `var(--text-primary)` |
| Answer reveal | 56px | 800 | On colored background, with pulse animation |
| Detail text | 13px | 400 | Below answer or on back |
| SVG labels on dots | 10-11px | 500-700 | White on colored dot |
| Small chips / tags | 9-11px | 600 | Chord tags, step indicators |
| Button text | 13-15px | 500-600 | Action and grid buttons |

### Mobile Overrides

```css
@media (max-width: 400px) {
  .name   { font-size: 20px; }    /* was 24px */
  .answer { font-size: 36-42px; } /* was 56px */
  .btn    { font-size: 11-13px; } /* was 13-15px */
  /* padding reduced ~15-20% across the board */
}
```

---

## 3. Card Structure

### Layout Flow

Every card follows this top-to-bottom structure:

```
+------------------------------------------+
| Tag Bar                    (bg-subtle)   |
+------------------------------------------+
| Question Label             (14px, secondary) |
+------------------------------------------+
| Content Block              (the visual)  |
| (SVG / interactive area / song block)    |
+------------------------------------------+
| Answer Section (back only) (bg-subtle    |
|   or color-coded)                        |
+------------------------------------------+
```

### Tag Bar

```css
.tag {
  color: var(--text-secondary);
  font-size: 16px;
  background-color: var(--bg-subtle);
  padding: 2px 8px;
  border-radius: 5px;
  display: table;        /* auto-width, shrink-wraps content */
  margin-bottom: 12px;
}
```

Content: emoji + domain label, e.g. "&#127928; Fretboard", "&#127932; Sheet Music", "&#127929; Piano"

### Question Label (Prompt)

```css
.prompt {
  font-size: 14px;
  color: var(--text-secondary);
  margin-bottom: 10px;
}
```

Recognition front: "What is this?"
Recall front: "Place the notes on the fretboard:"

### Content Block (Song/Source Blocks)

Clickable content blocks use this pattern for hover feedback:

```css
.content-block {
  background: var(--bg-subtle);
  cursor: pointer;
  border-radius: 10px;
  padding: 14px 20px;
  margin-bottom: 10px;
  transition: background 0.2s ease;
}

.content-block:hover, .content-block:active {
  background: var(--bg-chip);
}
```

### Answer Section

```css
.answer-section {
  padding: 14-24px 16px;
  background: var(--bg-subtle);  /* or color-coded with inline style */
  border-radius: 10px;
  margin-top: 14px;
  text-align: center;
  cursor: pointer;
  transition: filter 0.2s ease;
}

.answer-section:hover, .answer-section:active {
  filter: brightness(1.1);
}
```

Text hierarchy within the answer section (on colored background):
- `.note-label`: 13px, `rgba(255,255,255,0.6)` -- category label
- `.note-reveal`: 56px, weight 800, `#fff` -- the answer
- `.note-detail`: 13px, `rgba(255,255,255,0.5)` -- supporting info
- `.tap-hint`: 13px, `rgba(255,255,255,0.35)` -- interaction hint

**No celebration text.** Just show the answer. No "Correct!", "Perfect!", or gamification language.

---

## 4. Interactive Elements

### Buttons / Chips

Base button pattern used for grid buttons, action buttons, and selection chips:

```css
.btn {
  font-family: Nunito, sans-serif;
  font-size: 15px;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 8px;
  border: 0.5px solid var(--border-dashed);
  background: var(--bg-subtle);
  color: var(--text-secondary);
  cursor: pointer;
  min-height: 40px;
  transition: all 0.15s ease;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  -webkit-user-select: none;
}
```

### Interaction States

```css
/* Selected (user picked this option) */
.btn.selected {
  background: var(--accent);
  color: var(--accent-text);
  border-color: var(--accent);
  font-weight: 700;
}

/* Correct (revealed after check) */
.btn.correct {
  background: var(--green);
  color: #fff;
  border-color: var(--green);
}

/* Wrong (revealed after check) */
.btn.wrong {
  background: var(--red);
  color: #fff;
  border-color: var(--red);
}

/* Disabled (locked section, already answered) */
.btn.disabled {
  opacity: 0.3;
  pointer-events: none;
}

/* Active press */
.btn:active {
  background: var(--bg-chip);
}

/* Desktop hover only */
@media (hover: hover) {
  .btn:hover {
    background: var(--bg-chip);
    border-color: var(--border-dashed);
  }
}
```

### Touch-Friendly Sizing

- Minimum tap target: 40-44px height, 44px width for key grid buttons
- `touch-action: manipulation` on all buttons (prevents double-tap zoom)
- `-webkit-tap-highlight-color: transparent` (removes iOS blue flash)
- `-webkit-appearance: none` on styled buttons (consistent cross-platform)

### Sequence Chips (Ordered Selection)

For cards where the user builds an ordered answer:

```css
.seq-chip {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 14px;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 8px;
  background: var(--bg-chip);
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.15s ease;
}
```

### Locked / Unlocking Sections

Some cards have multi-step flows where sections unlock progressively:

```css
.section {
  background: var(--bg-subtle);
  border-radius: 10px;
  padding: 16px 20px;
  opacity: 0.3;
  pointer-events: none;
  transition: opacity 0.3s;
}

.section.unlocked {
  opacity: 1;
  pointer-events: auto;
}
```

---

## 5. Animation Patterns

### Answer Reveal Pulse

The signature animation when the answer appears on the back side:

```css
@keyframes keyPulse {
  0%   { transform: scale(0.8); opacity: 0; }
  50%  { transform: scale(1.05); }
  100% { transform: scale(1.0); opacity: 1; }
}

.note-reveal {
  animation: keyPulse 0.5s ease-out;
}
```

### Hover Transitions

Standard duration for background color changes on interactive elements:

```css
transition: all 0.15s ease;          /* buttons, chips */
transition: background 0.2s ease;    /* content blocks */
transition: filter 0.2s ease;        /* answer section brightness */
transition: opacity 0.2s ease;       /* replay buttons, hints */
```

### Section Unlock Fade

When a locked section becomes active:

```css
transition: opacity 0.3s;  /* from 0.3 to 1.0 */
```

### Ghost Elements (Recall Mode Hover Preview)

On desktop, hovering over a tap zone shows a faint preview of what would be placed:

```css
.ghost-note {
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.1s;
}

.tap-zone:hover + .ghost-note {
  opacity: 0.25;
}
```

For multi-element ghosts (e.g. a note head + ledger lines), wrap in `<g class="ghost-group">` and use:

```css
.ghost-group { opacity: 0; pointer-events: none; transition: opacity 0.1s; }
.tap-zone:hover + .ghost-group { opacity: 0.25; }
```

### Pulsing Ring (Single Unknown Note)

When a single dot is shown without a label (recognition front for a single note):

```xml
<circle cx="X" cy="Y" r="10" fill="var(--accent)"/>
<!-- Pulsing ring expanding outward -->
<circle cx="X" cy="Y" r="10" fill="none" stroke="var(--accent)" stroke-width="2" opacity="0.4">
  <animate attributeName="r" from="10" to="20" dur="2s" repeatCount="indefinite"/>
  <animate attributeName="opacity" from="0.4" to="0" dur="2s" repeatCount="indefinite"/>
</circle>
```

### Button Press Scale

For grid cells in progression answers:

```css
.cell:active, .cell.playing {
  transform: scale(0.93);
  opacity: 0.7;
}
```

---

## 6. SVG Patterns

### General Principles

- All instruments/visuals rendered as **inline SVGs** with `viewBox` for responsive scaling
- Cap size with `max-width` (540px for fretboard, varies by domain)
- All colors use **CSS custom properties** (they work inside inline SVG within HTML)
- Render **interactive elements (tap zones) LAST** in the SVG source so they sit on top in z-order
- Use `pointer-events: none` on decorative overlays and placed dots

### Tap Zones

Invisible hit areas layered on top of the visual:

```javascript
// Transparent circles as tap targets, rendered AFTER visible elements
svg += '<circle class="tap-zone" cx="' + cx + '" cy="' + cy + '" r="' + hitRadius + '"'
     + ' fill="transparent" data-id="' + id + '"'
     + ' onclick="onTap(\'' + id + '\')"/>';
```

```css
.tap-zone {
  cursor: pointer;
  transition: opacity 0.15s;
}
.tap-zone:hover { opacity: 0.8; }
```

### Placed Dots (User's Answer in Recall Mode)

```css
.placed-dot {
  pointer-events: none;  /* clicks pass through to tap-zone beneath */
}
```

### Root Indicators

Roots are shown with a **ring outline**, not a bigger dot:

```javascript
if (isRoot && dots.length > 1) {
  svg += '<circle cx="' + cx + '" cy="' + cy + '" r="' + (r + 4) + '"'
       + ' fill="none" stroke="' + fill + '" stroke-width="1.5" opacity="0.5"/>';
}
```

### Labels on Dots

White text centered on colored circles, shown only on the back side:

```javascript
svg += '<text x="' + cx + '" y="' + (cy + 4) + '"'
     + ' text-anchor="middle" font-size="11" font-weight="700"'
     + ' fill="#fff" font-family="Nunito,sans-serif">' + label + '</text>';
```

### Result Overlay (Back Side of Recall)

Three classes for comparing user's answer to the correct answer:

```css
.dot-correct {
  fill: var(--green);
}

.dot-wrong {
  fill: var(--red);
}

.dot-missing {
  fill: none;
  stroke: var(--red);
  stroke-width: 2;
  stroke-dasharray: 4 2;
}
```

Green dots get a checkmark, red dots get an X, missing dots get a dashed outline ring.

### Interval Coloring

When dots are color-coded by their interval function (chords, scales):

| Interval | Color | CSS |
|----------|-------|-----|
| Root (1) | `var(--accent)` | Blue-teal |
| Minor 3rd (b3) | `#e8a030` | Warm orange |
| Major 3rd (3) | `#e8a030` | Warm orange |
| Perfect 5th (5) | `#5a8abf` | Cool blue |
| Minor 7th (b7) | `#9b59b6` | Purple |
| Major 7th (7) | `#c0392b` | Red |

---

## 7. Card Type Pattern (Recognition + Recall)

### Core Principle

Every note type produces **two card types** from the same set of fields:

- **Card 1 (Recognition):** See the visual, identify or name it
- **Card 2 (Recall):** See the name, reproduce the visual by tapping

### Card 1: Recognition

**Front:**
- Tag bar
- Prompt: "What is this?"
- The visual (SVG) showing the item with dots/shapes but no labels
- Single-note items get a pulsing ring animation
- Tapping plays audio at that position (feedback only, not graded)

**Back:**
- Tag bar
- Prompt repeated
- The visual again, now with **labels on every dot**
- Answer section (color-coded background) with:
  - Category label (small, semi-transparent)
  - The answer in large text (56px, pulse animation)
  - Supporting detail (intervals, position info)
  - "tap to play" hint

### Card 2: Recall

**Front:**
- Tag bar
- Prompt: "Place the notes on the [domain]:"
- Name/title in large text (24px bold)
- Blank interactive area (empty fretboard/keyboard/staff)
- User taps to place dots; tapping again removes them
- No separate undo/clear buttons in simple recall

**Back:**
- Tag bar
- Name repeated
- Result overlay on the visual:
  - **Green dots**: correct placements
  - **Red dots**: wrong placements
  - **Dashed outlines**: missing (expected but not placed)
- Answer section (same as Recognition back)

### Order Sensitivity

Controlled by the `Type` field:
- `"chord"`: order does NOT matter -- any permutation of correct positions is accepted
- `"scale"`, `"arpeggio"`: order DOES matter -- dots get numbered labels showing sequence

### Result Comparison Logic

```javascript
// For unordered types (chords):
// Compare sets: each placed dot is correct if it matches any expected dot

// For ordered types (scales/arpeggios):
// Compare sequences: placed[i] must match expected[i]

// Result categories:
// correct = placed dot matches an expected dot
// wrong   = placed dot doesn't match any expected dot
// missing = expected dot not covered by any placed dot
```

---

## 8. Audio

### Web Audio API Pattern

All audio uses `AudioContext` with `OscillatorNode`. No audio files.

```javascript
var ctx = new (window.AudioContext || window.webkitAudioContext)();
if (ctx.state === 'suspended') ctx.resume();  // required for mobile

var freq = 440 * Math.pow(2, (midi - 69) / 12);  // equal temperament from A4=440Hz
var now = ctx.currentTime;
```

### Quick Tone (Single Note)

Duration ~1.5s with exponential decay:

```javascript
var g = ctx.createGain();
g.gain.setValueAtTime(0.3, now);
g.gain.exponentialRampToValueAtTime(0.001, now + 1.5);
g.connect(ctx.destination);

var osc = ctx.createOscillator();
osc.type = 'triangle';
osc.frequency.setValueAtTime(freq, now);
osc.connect(g);
osc.start(now);
osc.stop(now + 1.5);
```

### Guitar Timbre (Dual Oscillator)

Adds a soft harmonic overtone for a richer sound:

```javascript
// Fundamental
var osc1 = ctx.createOscillator();
osc1.type = 'triangle';
osc1.frequency.setValueAtTime(freq, now);

// 2nd harmonic (octave above, much quieter)
var osc2 = ctx.createOscillator();
osc2.type = 'triangle';
osc2.frequency.setValueAtTime(freq * 2, now);

// Gains: fundamental 0.3, overtone 0.08
// Decay: fundamental 1.5s, overtone 1.0s
```

### Playback Conventions

- Tap on front side: play the note at the tapped position (feedback)
- Tap on answer section (back): replay the answer note/chord
- Auto-play on back reveal: 200ms delay after page loads
- Strum/arpeggio: stagger notes by 50-80ms each

---

## 9. Responsive Design

### Max Width Container

```css
.card-body {
  max-width: 520px;  /* or up to 540px for wide instruments */
}

svg {
  width: 100%;
  max-width: 540px;
}
```

### Mobile Breakpoint

```css
@media (max-width: 400px) {
  /* Reduce title: 24px -> 20px */
  /* Reduce answer: 56px -> 36-42px */
  /* Reduce buttons: padding 8px 16px -> 7px 12px, font 15px -> 11-13px */
  /* Reduce gaps: 8px -> 6px */
  /* Reduce table cells: padding 6px 10px -> 4px 8px */
}
```

### Desktop-Only Hover

```css
@media (hover: hover) {
  .btn:hover { background: var(--bg-chip); }
  .white-key:hover { fill: #e8e8e8; }
  .black-key:hover { fill: #444; }
  .chord-play:hover { color: var(--accent); }
}
```

This prevents hover styles from "sticking" on mobile after a tap.

### Grid Layouts

For button grids with variable number of items:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(N, 1fr);
  gap: 4-8px;
  width: 100%;
}

/* Or flex-wrap for variable-width buttons: */
.flex-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
```

### Overflow Handling

For wide instruments (piano keyboard):

```css
.instrument-wrap {
  overflow-x: auto;
  margin: 0 -8px;
  padding: 0 8px;
}
```

---

## 10. Data Format

### Tab-Separated Text Files

- No header row (Anki import expects raw data)
- One entry per line
- Fields separated by tabs, matching the Anki note type field order
- Each line produces both Recognition and Recall cards automatically

### Common Field Patterns

| Field | Purpose | Example |
|-------|---------|---------|
| Type | Card category (controls behavior) | `"note"`, `"chord"`, `"scale"`, `"arpeggio"` |
| Name | Display name / the answer | `"Am Pentatonic Pos 1"` |
| Dots / Positions | Encoded locations | `"6-5,5-5,5-7"` (string-fret) |
| Root | Primary reference point | `"6-5"` |
| Notes / Labels | Display names per position | `"A,D,E,G"` |
| Shape | Pattern/system name | `"CAGED E shape"` |
| Key | Color coding key | `"Am"` |
| Intervals | Functional labels | `"1,b3,4,5,b7"` |
| Tags | Anki tags | `Instrument::Guitar Key::Am` |

### Position Encoding by Domain

| Domain | Format | Example |
|--------|--------|---------|
| Fretboard | `string-fret` pairs | `"6-5,5-5,4-5,4-7"` |
| Piano | Note names | `"C4,E4,G4"` |
| Sheet Music | Note names with octave | `"E4,G4,B4"` |
| General | Depends on SVG coordinate system | `"x-y"` pairs or element IDs |

### Tags

Tags use the Anki convention (no spaces within a tag, spaces separate tags):

```
Instrument::Guitar Type::Scale Key::Am Shape::Pentatonic
```

---

## 11. Applying to New Domains

### What to Keep (Universal)

These elements are domain-agnostic and should be reused exactly:

1. **Color system** -- all CSS custom properties, light/dark mode, both night mode selectors
2. **Typography** -- Nunito font stack, size scale, weight conventions
3. **Card structure** -- tag bar, question label, content block, answer section
4. **Answer section** -- color-coded background, pulse animation, text hierarchy, no celebration text
5. **Button/chip patterns** -- bg-subtle with border-dashed, states (selected/correct/wrong/disabled)
6. **Animation patterns** -- keyPulse, hover transitions, ghost previews, section unlock fades
7. **Touch-friendly sizing** -- min 40-44px targets, touch-action manipulation, tap highlight transparent
8. **Responsive breakpoints** -- max-width 520px, @media 400px, @media hover:hover
9. **Recognition + Recall card type pattern** -- two cards from one note type

### What to Swap (Domain-Specific)

1. **SVG renderer** -- replace fretboard/keyboard/staff with map, molecule, diagram, circuit, etc.
2. **Position encoding** -- define how positions are serialized for the new domain
3. **Domain-specific CSS variables** -- add `--wire-color`, `--membrane-opacity`, etc. alongside the universal variables
4. **Audio engine** -- optional; replace with domain-appropriate feedback or remove
5. **Color mapping** -- adapt the 12-color palette or define a new categorical palette
6. **Tag emoji + label** -- e.g. "&#127758; Geography", "&#129514; Chemistry", "&#128300; Anatomy"

### Template: New Domain Checklist

```
[ ] Define the visual (what SVG represents the domain?)
[ ] Define positions (how are answer locations encoded?)
[ ] Map categories to color palette
[ ] Build SVG renderer with:
    [ ] viewBox responsive scaling
    [ ] CSS variable colors
    [ ] Tap zones rendered LAST (z-order)
    [ ] Ghost previews for recall mode
    [ ] Root/primary indicators (ring outline)
    [ ] Result overlay (green/red/dashed)
[ ] Wire up Card 1 (Recognition):
    [ ] Front: tag + prompt + visual (no labels)
    [ ] Back: tag + prompt + visual (with labels) + answer section
[ ] Wire up Card 2 (Recall):
    [ ] Front: tag + prompt + name + blank interactive area
    [ ] Back: tag + name + result overlay + answer section
[ ] Generate tab-separated data file
[ ] Build preview page with mode tabs and controls
[ ] Test dark mode (both .night_mode and .nightMode)
[ ] Test mobile (max-width: 400px)
[ ] Test hover vs touch (@media hover:hover)
```

### File Naming Convention

```
{domain}_card_style.css      -- Anki CSS (shared by both card types)
{domain}_front1.html         -- Card 1 front (Recognition)
{domain}_back1.html          -- Card 1 back  (Recognition)
{domain}_front2.html         -- Card 2 front (Recall)
{domain}_back2.html          -- Card 2 back  (Recall)
{domain}_preview.html        -- Interactive preview page
{domain}_cards.txt           -- Tab-separated data file
generate_{domain}_data.py    -- Data generation script
{DOMAIN}_CARD_DESIGN.md      -- Domain-specific design doc
```

### Example: Geography Cards

Applying this system to a geography domain:

- **Visual:** SVG world/region map with clickable country/state paths
- **Positions:** Country ISO codes or path IDs
- **Colors:** By continent (7-color palette)
- **Card 1 (Recognition):** Highlighted country on map -> "What country is this?"
- **Card 2 (Recall):** Country name shown -> tap on the correct region
- **Answer section:** Colored by continent, shows capital + population + flag
- **Ghost preview:** Faint highlight of hovered region
- **Result overlay:** Green fill (correct country), red fill (wrong tap), dashed outline (missed)

### Copy-Paste Starter CSS

```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

.card {
  font-family: Nunito, -apple-system, 'Segoe UI', sans-serif;
  font-size: 22px;
  text-align: left;
  background: #FFFAF0;
  color: #333;
  -webkit-text-size-adjust: 100%;
  --green: #3a9a5a;
  --red: #c75050;
  --accent: #4ba9c8;
  --accent-text: #fff;
  --text-primary: #333;
  --text-secondary: rgba(0,0,0,0.45);
  --bg-subtle: rgba(0,0,0,0.06);
  --bg-chip: rgba(0,0,0,0.12);
  --border-dashed: rgba(0,0,0,0.12);
}

.night_mode.card, .night_mode .card {
  background: #333b45;
  color: #e6e6e6;
  --green: #5db87a;
  --red: #c75a5a;
  --accent: #4ba9c8;
  --accent-text: #1a2530;
  --text-primary: #e6e6e6;
  --text-secondary: rgba(255,255,255,0.45);
  --bg-subtle: rgba(255,255,255,0.08);
  --bg-chip: rgba(255,255,255,0.15);
  --border-dashed: rgba(255,255,255,0.15);
}

.nightMode.card, .nightMode .card {
  background: #333b45;
  color: #e6e6e6;
  --green: #5db87a;
  --red: #c75a5a;
  --accent: #4ba9c8;
  --accent-text: #1a2530;
  --text-primary: #e6e6e6;
  --text-secondary: rgba(255,255,255,0.45);
  --bg-subtle: rgba(255,255,255,0.08);
  --bg-chip: rgba(255,255,255,0.15);
  --border-dashed: rgba(255,255,255,0.15);
}

.tag {
  color: var(--text-secondary);
  font-size: 16px;
  background-color: var(--bg-subtle);
  padding: 2px 8px;
  border-radius: 5px;
  display: table;
  margin-bottom: 12px;
}

.prompt {
  font-size: 14px;
  color: var(--text-secondary);
  margin-bottom: 10px;
}

.name {
  font-size: 24px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 10px;
}

.answer-section {
  padding: 24px 16px;
  background: var(--bg-subtle);
  border-radius: 10px;
  margin-top: 14px;
  text-align: center;
  cursor: pointer;
  transition: filter 0.2s ease;
}

.answer-section:hover, .answer-section:active {
  filter: brightness(1.1);
}

@keyframes keyPulse {
  0%   { transform: scale(0.8); opacity: 0; }
  50%  { transform: scale(1.05); }
  100% { transform: scale(1.0); opacity: 1; }
}

.note-reveal {
  font-size: 56px;
  font-weight: 800;
  color: #fff;
  animation: keyPulse 0.5s ease-out;
}

.note-label {
  font-size: 13px;
  color: rgba(255,255,255,0.6);
  margin-bottom: 8px;
}

.tap-hint {
  font-size: 13px;
  color: rgba(255,255,255,0.35);
  margin-top: 6px;
}

.tap-zone { cursor: pointer; transition: opacity 0.15s; }
.tap-zone:hover { opacity: 0.8; }
.placed-dot { pointer-events: none; }

.ghost-note { opacity: 0; pointer-events: none; transition: opacity 0.1s; }
.tap-zone:hover + .ghost-note { opacity: 0.25; }

.dot-correct { fill: var(--green); }
.dot-wrong   { fill: var(--red); }
.dot-missing { fill: none; stroke: var(--red); stroke-width: 2; stroke-dasharray: 4 2; }

.recall-action-btn {
  font-family: Nunito, sans-serif;
  font-size: 13px;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  min-height: 36px;
  background: var(--bg-subtle);
  color: var(--text-secondary);
  transition: all 0.15s ease;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

@media (hover: hover) {
  .recall-action-btn:hover { opacity: 0.7; }
}

@media (max-width: 400px) {
  .name { font-size: 20px; }
  .note-reveal { font-size: 42px; }
  .recall-action-btn { padding: 7px 12px; font-size: 11px; }
}
```
