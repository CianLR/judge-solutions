import sys

alts = {
    'A': None,
    'A#': 'Bb',
    'Bb': 'A#',
    'B': None,
    'C': None,
    'C#': 'Db',
    'Db': 'C#',
    'D': None,
    'D#': 'Eb',
    'Eb': 'D#',
    'E': None,
    'F': None,
    'F#': 'Gb',
    'Gb': 'F#',
    'G': None,
    'G#': 'Ab',
    'Ab': 'G#'
}


for i, line in enumerate(sys.stdin.readlines()):
    note, key = line.split()
    alt = alts[note]
    if alt:
        print("Case {}: {} {}".format(i + 1, alt, key))
    else:
        print("Case {}: UNIQUE".format(i + 1))
