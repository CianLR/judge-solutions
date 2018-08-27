NUMS = """
xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx
....x
....x
....x
....x
....x
....x
....x
xxxxx
....x
....x
xxxxx
x....
x....
xxxxx
xxxxx
....x
....x
xxxxx
....x
....x
xxxxx
x...x
x...x
x...x
xxxxx
....x
....x
....x
xxxxx
x....
x....
xxxxx
....x
....x
xxxxx
xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx
xxxxx
....x
....x
....x
....x
....x
....x
xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx
xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx
.....
..x..
..x..
xxxxx
..x..
..x..
.....
"""
CHAR_MAP = {
    tuple(NUMS.split()[i*7:(i+1)*7]): i for i in range(len(NUMS.split()) // 7)
}

def ident_char(char):
    return CHAR_MAP[tuple(char)]

def convert_int(i):
    for char, val in CHAR_MAP.items():
        if val == i:
            return char

def list_to_int(lst):
    i = 0
    for c in lst:
        i = (i * 10) + c
    return i

def int_to_chars(i):
    parts = []
    while i:
        i, ic = divmod(i, 10)
        parts.append(convert_int(ic))
    parts = parts[::-1]
    return [
        '.'.join(parts[p][l] for p in range(len(parts))) for l in range(7)
    ]

def evaluate(chars):
    conv_chars = [ident_char(c) for c in chars]
    plus = conv_chars.index(10)
    a = list_to_int(conv_chars[:plus])
    b = list_to_int(conv_chars[plus+1:])
    final = a + b
    return int_to_chars(final)


def main():
    lines = [input() for _ in range(7)]
    chars = [[l[i:i+5] for l in lines] for i in range(0, len(lines[0]), 6)]
    for line in evaluate(chars):
        print(line)

if __name__ == '__main__':
    main()

