import sys

def is_jolly(seq):
    has = [False] * (len(seq) - 1)
    should_be = ((len(seq) - 1) * len(seq)) / 2
    for a, b in zip(seq, seq[1:]):
        d = abs(a - b) - 1
        if d < 0 or d >= len(has) or has[d]:
            return False
        has[d] = True
    return True

def main():
    for line in sys.stdin.readlines():
        seq = [int(x) for x in line.split()[1:]]
        print "Jolly" if is_jolly(seq) else "Not jolly"

if __name__ == '__main__':
    main()
