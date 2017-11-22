
vals = {chr(c): c - ord('A') for c in range(ord('A'), ord('Z') + 1)}
chrs = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

def score(s):
    return sum(vals[c] for c in s)

def rotate(s, n):
    return ''.join(chrs[(vals[c] + n) % len(chrs)] for c in s)


instr = input()
first, second = instr[:len(instr) // 2], instr[len(instr) // 2:]
first, second = rotate(first, score(first)), rotate(second, score(second))

final = ''.join(rotate(fc, score(sc)) for fc, sc in zip(first, second))
print(final)

