import sys

codes = {
    'A': '.-',
    'H': '....',
    'O': '---',
    'V': '...-',
    'B': '-...',
    'I': '..',
    'P': '.--.',
    'W': '.--',
    'C': '-.-.',
    'J': '.---',
    'Q': '--.-',
    'X': '-..-',
    'D': '-..',
    'K': '-.-',
    'R': '.-.',
    'Y': '-.--',
    'E': '.',
    'L': '.-..',
    'S': '...',
    'Z': '--..',
    'F': '..-.',
    'M': '--',
    'T': '-',  
    'G': '--.',
    'N': '-.',
    'U': '..-',
    '_': '..--',
    '.': '---.',
    ',': '.-.-',
    '?': '----'
}

rev_codes = {v: k for k, v in codes.items()}

for l in sys.stdin.readlines():
    l = l.strip()
    coded = ''.join([codes[c] for c in l])
    code_lens = [len(codes[c]) for c in l][::-1]
    decoded = ''
    for code_lenght in code_lens:
        code = coded[:code_lenght]
        coded = coded[code_lenght:]
        decoded += rev_codes[code]
    print(decoded)
