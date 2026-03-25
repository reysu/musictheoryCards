#!/usr/bin/env python3
"""Generate fretboard card data with intervals."""

CHROMATIC = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
TUNING = {1:'E', 2:'B', 3:'G', 4:'D', 5:'A', 6:'E'}  # string -> open note

INTERVAL_NAMES = ['1','b2','2','b3','3','4','b5','5','b6','6','b7','7']

def note_at(string, fret):
    base = CHROMATIC.index(TUNING[string])
    return CHROMATIC[(base + fret) % 12]

def interval_between(root, note):
    ri = CHROMATIC.index(root)
    ni = CHROMATIC.index(note)
    return INTERVAL_NAMES[(ni - ri) % 12]

def parse_dots(dots_str):
    """Parse '6-5,5-7' into [(6,5),(5,7)]"""
    result = []
    for pair in dots_str.split(','):
        s, f = pair.strip().split('-')
        result.append((int(s), int(f)))
    return result

def compute_intervals(dots_str, root_str, key_root=None):
    """Compute intervals for each dot relative to the root note."""
    dots = parse_dots(dots_str)
    root_dot = parse_dots(root_str)[0]
    root_note = key_root or note_at(root_dot[0], root_dot[1])
    intervals = []
    for s, f in dots:
        note = note_at(s, f)
        intervals.append(interval_between(root_note, note))
    return ','.join(intervals)

lines = []

# 1. SINGLE NOTES (78)
for string in range(1, 7):
    for fret in range(0, 13):
        note = note_at(string, fret)
        dot = f"{string}-{fret}"
        lines.append(f"note\t{note}\t{dot}\t{dot}\t{note}\t\t\t")

# 2. Am PENTATONIC - 5 Positions
am_pent = [
    ("Am Pentatonic Pos 1", "6-5,6-8,5-5,5-7,4-5,4-7,3-5,3-7,2-5,2-8,1-5,1-8", "6-5", "Position 1", "Am"),
    ("Am Pentatonic Pos 2", "6-8,6-10,5-7,5-10,4-7,4-10,3-7,3-9,2-8,2-10,1-8,1-10", "4-7", "Position 2", "Am"),
    ("Am Pentatonic Pos 3", "6-10,6-12,5-10,5-12,4-10,4-12,3-9,3-12,2-10,2-12,1-10,1-12", "5-12", "Position 3", "Am"),
    ("Am Pentatonic Pos 4", "6-0,6-3,5-0,5-3,4-0,4-2,3-0,3-2,2-0,2-3,1-0,1-3", "5-0", "Position 4", "Am"),
    ("Am Pentatonic Pos 5", "6-3,6-5,5-3,5-5,4-2,4-5,3-2,3-5,2-3,2-5,1-3,1-5", "6-5", "Position 5", "Am"),
]

for name, dots, root, shape, key in am_pent:
    notes = ','.join([note_at(s, f) for s, f in parse_dots(dots)])
    intervals = compute_intervals(dots, root, 'A')
    lines.append(f"scale\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\t{shape}\t{key}")

# 3. Em PENTATONIC - 5 Positions
em_pent = [
    ("Em Pentatonic Pos 1", "6-0,6-3,5-0,5-2,4-0,4-2,3-0,3-2,2-0,2-3,1-0,1-3", "6-0", "Position 1", "Em"),
    ("Em Pentatonic Pos 2", "6-3,6-5,5-2,5-5,4-2,4-5,3-2,3-4,2-3,2-5,1-3,1-5", "5-5", "Position 2", "Em"),
    ("Em Pentatonic Pos 3", "6-5,6-7,5-5,5-7,4-5,4-7,3-4,3-7,2-5,2-8,1-5,1-7", "4-7", "Position 3", "Em"),
    ("Em Pentatonic Pos 4", "6-7,6-10,5-7,5-9,4-7,4-9,3-7,3-9,2-8,2-10,1-7,1-10", "5-9", "Position 4", "Em"),
    ("Em Pentatonic Pos 5", "6-10,6-12,5-9,5-12,4-9,4-12,3-9,3-12,2-10,2-12,1-10,1-12", "6-12", "Position 5", "Em"),
]

for name, dots, root, shape, key in em_pent:
    notes = ','.join([note_at(s, f) for s, f in parse_dots(dots)])
    intervals = compute_intervals(dots, root, 'E')
    lines.append(f"scale\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\t{shape}\t{key}")

# 4. BB KING / ALBERT KING / SRV BOXES (in Am)
blues_boxes = [
    ("BB King Box (Am)", "2-5,2-8,1-5,1-8,1-5,2-6,2-5", "1-5",
     # Simplified: key positions BB favors - strings 1-2, frets 5-8
     "6-5,5-5,4-5,3-5,3-6,2-5,2-6,2-8,1-5,1-8", "6-5",
     "BB King Box", "Am"),
    ("Albert King Box (Am)", "6-3,6-5,5-3,5-5,4-2,4-5,3-2,3-5,2-3,2-5,1-3,1-5", "6-5",
     "Albert King Box", "Am"),
    ("SRV Box (Am)", "6-5,6-8,5-5,5-7,5-8,4-5,4-7,3-5,3-7,3-8,2-5,2-8,1-5,1-8", "6-5",
     "SRV Box", "Am"),
]

# BB King Box - upper register, strings 1-3 around frets 5-8
bb_dots = "3-5,3-7,3-8,2-5,2-8,1-5,1-7,1-8"
bb_name = "BB King Box (Am)"
bb_notes = ','.join([note_at(s,f) for s,f in parse_dots(bb_dots)])
bb_intervals = compute_intervals(bb_dots, "1-5", "A")
lines.append(f"scale\t{bb_name}\t{bb_dots}\t1-5\t{bb_notes}\t{bb_intervals}\tBB King Box\tAm")

# Albert King Box - positions 4+5, strings 1-4
ak_dots = "4-2,4-5,3-2,3-5,2-3,2-5,1-3,1-5"
ak_name = "Albert King Box (Am)"
ak_notes = ','.join([note_at(s,f) for s,f in parse_dots(ak_dots)])
ak_intervals = compute_intervals(ak_dots, "1-5", "A")
lines.append(f"scale\t{ak_name}\t{ak_dots}\t1-5\t{ak_notes}\t{ak_intervals}\tAlbert King Box\tAm")

# SRV Box - bridges positions 1 and 2
srv_dots = "6-5,6-8,5-5,5-7,5-8,4-5,4-7,4-8,3-5,3-7,2-5,2-8,1-5,1-8"
srv_name = "SRV Box (Am)"
srv_notes = ','.join([note_at(s,f) for s,f in parse_dots(srv_dots)])
srv_intervals = compute_intervals(srv_dots, "6-5", "A")
lines.append(f"scale\t{srv_name}\t{srv_dots}\t6-5\t{srv_notes}\t{srv_intervals}\tSRV Box\tAm")

# 5. OPEN CHORDS
chords = [
    ("C major", "5-3,4-2,3-0,2-1,1-0", "5-3", "Open C", "C", "C"),
    ("D major", "4-0,3-2,2-3,1-2", "4-0", "Open D", "D", "D"),
    ("E major", "6-0,5-2,4-2,3-1,2-0,1-0", "6-0", "Open E", "E", "E"),
    ("G major", "6-3,5-2,4-0,3-0,2-0,1-3", "6-3", "Open G", "G", "G"),
    ("A major", "5-0,4-2,3-2,2-2,1-0", "5-0", "Open A", "A", "A"),
    ("Am", "5-0,4-2,3-2,2-1,1-0", "5-0", "Open Am", "Am", "A"),
    ("Dm", "4-0,3-2,2-3,1-1", "4-0", "Open Dm", "Dm", "D"),
    ("Em", "6-0,5-2,4-2,3-0,2-0,1-0", "6-0", "Open Em", "Em", "E"),
    ("F major", "6-1,5-3,4-3,3-2,2-1,1-1", "6-1", "F barre", "F", "F"),
    ("B7", "5-2,4-1,3-2,2-0,1-2", "5-2", "Open B7", "B", "B"),
]

for name, dots, root, shape, key, root_note in chords:
    notes = ','.join([note_at(s,f) for s,f in parse_dots(dots)])
    intervals = compute_intervals(dots, root, root_note)
    lines.append(f"chord\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\t{shape}\t{key}")

# 6. BARRE CHORDS
barres = [
    ("A barre (E-shape)", "6-5,5-7,4-7,3-6,2-5,1-5", "6-5", "E-shape barre", "A", "A"),
    ("C barre (A-shape)", "5-3,4-5,3-5,2-5,1-3", "5-3", "A-shape barre", "C", "C"),
    ("Am barre (Em-shape)", "6-5,5-7,4-7,3-5,2-5,1-5", "6-5", "Em-shape barre", "Am", "A"),
    ("Cm barre (Am-shape)", "5-3,4-5,3-5,2-4,1-3", "5-3", "Am-shape barre", "Cm", "C"),
]

for name, dots, root, shape, key, root_note in barres:
    notes = ','.join([note_at(s,f) for s,f in parse_dots(dots)])
    intervals = compute_intervals(dots, root, root_note)
    lines.append(f"chord\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\t{shape}\t{key}")

# 7. TRIADS (major, minor, diminished - across strings)
# String groups: (6,5,4), (5,4,3), (4,3,2), (3,2,1)
# Root position, 1st inversion, 2nd inversion for each
triad_defs = {
    'major': {'intervals': [0, 4, 7], 'names': ['1','3','5']},
    'minor': {'intervals': [0, 3, 7], 'names': ['1','b3','5']},
    'dim': {'intervals': [0, 3, 6], 'names': ['1','b3','b5']},
    'aug': {'intervals': [0, 4, 8], 'names': ['1','3','#5']},
}

# Generate triads on common string sets, in key of C, G, A, D, E, F
triad_keys = [('C', 0), ('G', 7), ('A', 9), ('D', 2), ('E', 4), ('F', 5)]
string_sets = [(6,5,4), (5,4,3), (4,3,2), (3,2,1)]

for key_name, key_idx in triad_keys:
    for quality, qdata in [('major', triad_defs['major']), ('minor', triad_defs['minor'])]:
        suffix = '' if quality == 'major' else 'm'
        q_intervals = qdata['intervals']
        q_names = qdata['names']

        for si, string_set in enumerate(string_sets):
            # Root position: find frets for each note on each string
            frets = []
            for i, string in enumerate(string_set):
                target_note_idx = (key_idx + q_intervals[i]) % 12
                open_note_idx = CHROMATIC.index(TUNING[string])
                fret = (target_note_idx - open_note_idx) % 12
                # Prefer frets 0-12
                frets.append((string, fret))

            dots = ','.join([f"{s}-{f}" for s, f in frets])
            root = f"{frets[0][0]}-{frets[0][1]}"
            notes = ','.join([note_at(s,f) for s,f in frets])
            intervals = ','.join(q_names)
            sset_name = f"strings {string_set[0]}-{string_set[2]}"
            card_name = f"{key_name}{suffix} triad ({sset_name})"

            lines.append(f"chord\t{card_name}\t{dots}\t{root}\t{notes}\t{intervals}\t{sset_name}\t{key_name}{suffix}")

# 8. C MAJOR SCALE - 5 positions with intervals
cmaj_positions = [
    ("C Major Pos 1", "6-8,6-10,5-7,5-8,5-10,4-7,4-9,4-10,3-7,3-9,3-10,2-8,2-10,1-7,1-8,1-10", "6-8"),
    ("C Major Pos 2", "6-10,6-12,5-10,5-12,4-10,4-12,3-9,3-10,3-12,2-10,2-12,1-10,1-12", "5-12"),
    ("C Major Pos 3", "6-0,6-1,6-3,5-0,5-2,5-3,4-0,4-2,3-0,3-2,2-0,2-1,2-3,1-0,1-1,1-3", "5-3"),
    ("C Major Pos 4", "6-3,6-5,5-3,5-5,4-2,4-3,4-5,3-2,3-4,3-5,2-3,2-5,1-3,1-5", "4-3"),
    ("C Major Pos 5", "6-5,6-7,6-8,5-5,5-7,5-8,4-5,4-7,3-5,3-7,2-5,2-6,2-8,1-5,1-7,1-8", "6-8"),
]

for name, dots, root in cmaj_positions:
    notes = ','.join([note_at(s,f) for s,f in parse_dots(dots)])
    intervals = compute_intervals(dots, root, 'C')
    lines.append(f"scale\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\tPosition {name[-1]}\tC")

# 9. A NATURAL MINOR - 5 positions with intervals
amin_positions = [
    ("A Minor Pos 1", "6-5,6-7,6-8,5-5,5-7,5-8,4-5,4-7,3-5,3-7,2-5,2-6,2-8,1-5,1-7,1-8", "6-5"),
    ("A Minor Pos 2", "6-8,6-10,5-8,5-10,4-7,4-8,4-10,3-7,3-9,3-10,2-8,2-10,1-8,1-10", "4-7"),
    ("A Minor Pos 3", "6-10,6-12,5-10,5-12,4-10,4-12,3-9,3-10,3-12,2-10,2-12,1-10,1-12", "5-12"),
    ("A Minor Pos 4", "6-0,6-1,6-3,5-0,5-2,5-3,4-0,4-2,3-0,3-2,2-0,2-1,2-3,1-0,1-1,1-3", "5-0"),
    ("A Minor Pos 5", "6-3,6-5,5-3,5-5,4-2,4-3,4-5,3-2,3-4,3-5,2-3,2-5,1-3,1-5", "6-5"),
]

for name, dots, root in amin_positions:
    notes = ','.join([note_at(s,f) for s,f in parse_dots(dots)])
    intervals = compute_intervals(dots, root, 'A')
    lines.append(f"scale\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\tPosition {name[-1]}\tAm")

# 10. JAZZ ARPEGGIOS with intervals
arpeggios = [
    ("Cmaj7 arpeggio", "6-8,5-7,4-9,3-9,2-8,1-7", "6-8", "Root position", "C", "C",
     ['1','3','5','7','1','3']),
    ("Am7 arpeggio", "6-5,5-7,4-5,4-7,3-5,2-5", "6-5", "Root position", "Am", "A",
     ['1','b3','5','b7','1','b3']),
    ("Dm7 arpeggio", "5-5,4-7,3-5,3-7,2-6,1-5", "5-5", "Root position", "Dm", "D",
     ['1','b3','5','b7','1','b3']),
    ("G7 arpeggio", "6-3,5-2,4-5,3-4,2-3,1-3", "6-3", "Root position", "G", "G",
     ['1','3','5','b7','1','3']),
    ("Fmaj7 arpeggio", "6-1,5-3,4-2,3-2,2-1,1-0", "6-1", "Root position", "F", "F",
     ['1','3','5','7','1','3']),
    ("Em7 arpeggio", "6-0,5-2,4-0,3-0,2-0,1-0", "6-0", "Root position", "Em", "E",
     ['1','b3','5','b7','1','b3']),
    ("Bm7b5 arpeggio", "5-2,4-3,3-2,3-4,2-3,1-2", "5-2", "Root position", "Bm7b5", "B",
     ['1','b3','b5','b7','1','b3']),
    ("A7 arpeggio", "5-0,4-2,3-0,3-2,2-2,1-0", "5-0", "Root position", "A", "A",
     ['1','3','5','b7','1','3']),
]

for name, dots, root, shape, key, root_note, ivls in arpeggios:
    notes_list = [note_at(s,f) for s,f in parse_dots(dots)]
    notes = ','.join(notes_list)
    # Use provided intervals (more accurate than computing for 7th chords)
    intervals = ','.join(ivls)
    lines.append(f"arpeggio\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\t{shape}\t{key}")

# 11. DOMINANT 7TH ARPEGGIOS (all 12 keys, root on 6th string)
dom7_arps = []
for key_name, key_idx in [('C',0),('C#',1),('D',2),('Eb',3),('E',4),('F',5),('F#',6),('G',7),('Ab',8),('A',9),('Bb',10),('B',11)]:
    # Find root on 6th string
    root_fret = (key_idx - CHROMATIC.index('E')) % 12
    # Dom7 = 1, 3, 5, b7
    # Build across strings near root position
    third_idx = (key_idx + 4) % 12
    fifth_idx = (key_idx + 7) % 12
    b7_idx = (key_idx + 10) % 12

    # Find reasonable frets for each note near root_fret
    def find_fret(string, target_idx, near):
        base = CHROMATIC.index(TUNING[string])
        fret = (target_idx - base) % 12
        # Pick closest to 'near'
        while fret < near - 4: fret += 12
        while fret > near + 8: fret -= 12
        if fret < 0: fret += 12
        return fret

    dots_list = []
    dots_list.append((6, root_fret))
    dots_list.append((5, find_fret(5, third_idx, root_fret)))
    dots_list.append((4, find_fret(4, fifth_idx, root_fret)))
    dots_list.append((3, find_fret(3, b7_idx, root_fret)))
    dots_list.append((2, find_fret(2, key_idx, root_fret)))  # octave root
    dots_list.append((1, find_fret(1, third_idx, root_fret)))  # octave 3rd

    dots = ','.join([f"{s}-{f}" for s,f in dots_list])
    root = f"6-{root_fret}"
    notes = ','.join([note_at(s,f) for s,f in dots_list])
    intervals = '1,3,5,b7,1,3'
    name = f"{key_name}7 arpeggio"
    lines.append(f"arpeggio\t{name}\t{dots}\t{root}\t{notes}\t{intervals}\tRoot position\t{key_name}7")
    dom7_arps.append(name)

# 12. ii-V-I PATTERNS (common jazz keys)
# Each ii-V-I is 3 arpeggios connected: ii=m7, V=7, I=maj7
# We'll create cards that show all 3 shapes together
ii_v_i_keys = [
    ('C', 'Dm7', 'G7', 'Cmaj7'),
    ('G', 'Am7', 'D7', 'Gmaj7'),
    ('F', 'Gm7', 'C7', 'Fmaj7'),
    ('Bb', 'Cm7', 'F7', 'Bbmaj7'),
    ('Eb', 'Fm7', 'Bb7', 'Ebmaj7'),
    ('D', 'Em7', 'A7', 'Dmaj7'),
    ('A', 'Bm7', 'E7', 'Amaj7'),
]

for key_name, ii_name, v_name, i_name in ii_v_i_keys:
    key_idx = CHROMATIC.index(key_name) if key_name in CHROMATIC else {'Bb':10,'Eb':3}[key_name]

    # ii chord root = key + 2 semitones
    ii_root_idx = (key_idx + 2) % 12
    # V chord root = key + 7 semitones
    v_root_idx = (key_idx + 7) % 12
    # I chord root = key

    # Build ii (m7): 1 b3 5 b7
    def build_arp(root_idx, intervals_semi, near_fret):
        dots = []
        strings = [6, 5, 4, 3]
        for si, semi in enumerate(intervals_semi):
            target = (root_idx + semi) % 12
            s = strings[si]
            f = find_fret(s, target, near_fret)
            dots.append((s, f))
        return dots

    # Position near middle of neck (fret 5-8 area)
    ii_fret = (ii_root_idx - CHROMATIC.index('E')) % 12
    v_fret = (v_root_idx - CHROMATIC.index('E')) % 12

    ii_dots = build_arp(ii_root_idx, [0, 3, 7, 10], ii_fret)
    v_dots = build_arp(v_root_idx, [0, 4, 7, 10], v_fret)
    i_dots = build_arp(key_idx, [0, 4, 7, 11], (key_idx - CHROMATIC.index('E')) % 12)

    # ii card
    dots_str = ','.join([f"{s}-{f}" for s,f in ii_dots])
    root_str = f"{ii_dots[0][0]}-{ii_dots[0][1]}"
    notes_str = ','.join([note_at(s,f) for s,f in ii_dots])
    lines.append(f"arpeggio\t{ii_name} (ii of {key_name})\t{dots_str}\t{root_str}\t{notes_str}\t1,b3,5,b7\tii-V-I in {key_name}\t{key_name}")

    # V card
    dots_str = ','.join([f"{s}-{f}" for s,f in v_dots])
    root_str = f"{v_dots[0][0]}-{v_dots[0][1]}"
    notes_str = ','.join([note_at(s,f) for s,f in v_dots])
    lines.append(f"arpeggio\t{v_name} (V of {key_name})\t{dots_str}\t{root_str}\t{notes_str}\t1,3,5,b7\tii-V-I in {key_name}\t{key_name}")

    # I card
    dots_str = ','.join([f"{s}-{f}" for s,f in i_dots])
    root_str = f"{i_dots[0][0]}-{i_dots[0][1]}"
    notes_str = ','.join([note_at(s,f) for s,f in i_dots])
    lines.append(f"arpeggio\t{i_name} (I of {key_name})\t{dots_str}\t{root_str}\t{notes_str}\t1,3,5,7\tii-V-I in {key_name}\t{key_name}")

# Write output
output = '\n'.join(lines) + '\n'
with open('/Users/reysu/commonwords/fretboard_full_cards.txt', 'w') as f:
    f.write(output)

print(f"Generated {len(lines)} entries:")
print(f"  - Single notes: 78")
print(f"  - Pentatonic scales: {len(am_pent) + len(em_pent)}")
print(f"  - Blues boxes: 3")
print(f"  - Open chords: {len(chords)}")
print(f"  - Barre chords: {len(barres)}")
print(f"  - Triads: {len(triad_keys) * 2 * len(string_sets)}")
print(f"  - Major scale positions: {len(cmaj_positions)}")
print(f"  - Minor scale positions: {len(amin_positions)}")
print(f"  - Jazz arpeggios: {len(arpeggios)}")
print(f"  - Dominant 7th arpeggios: {len(dom7_arps)}")
print(f"  - ii-V-I patterns: {len(ii_v_i_keys) * 3}")
