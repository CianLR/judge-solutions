
def nearest(c, choices):
    min_char = min_dist = 100
    for ch in choices:
        d = abs(ord(c) - ord(ch))
        if d < min_dist:
            min_dist = d
            min_char = ch
    return min_char

HARD_CONSTS = ["b", "c", "d", "g", "k", "n", "p", "t"]
def nimion(s):
    assert s
    if s[0] not in HARD_CONSTS:
        s = nearest(s[0], HARD_CONSTS) + s[1:]
    firstsyl, *rest = s.split('-')
    tail = ''.join(rest)
    for const in HARD_CONSTS:
        tail = tail.replace(const, firstsyl[0])
    s = firstsyl + tail
    if s[-1] in HARD_CONSTS:
        s += nearest(s[-1], ['a', 'o', 'u']) + 'h'
    return s

def main():
    sent = input().lower().split()
    print(' '.join(nimion(w) for w in sent).capitalize())

if __name__ == '__main__':
    main()

