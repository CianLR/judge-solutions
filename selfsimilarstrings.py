from sys import stdin
from collections import defaultdict

def get_ss(s):
    subs = defaultdict(int)
    for degree in xrange(1, len(s)):
        subs.clear()
        for j in xrange(len(s) - (degree - 1)):
            subs[s[j:j + degree]] += 1
        for v in subs.values():
            if v < 2:
                return degree - 1
    return len(s) - 1

def main():
    for line in stdin.readlines():
        print get_ss(line.strip())


if __name__ == '__main__':
    main()

