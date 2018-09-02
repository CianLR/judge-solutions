import sys
import math

FLIPABLE = [0, 1, 2, 5, 6, 8, 9]
FLIPPED = {0: 0, 1: 1, 2: 2, 5: 5, 6: 9, 8: 8, 9: 6}
BASE = len(FLIPABLE)

def flip(digits):
    return ''.join(map(str, (FLIPPED[d] for d in reversed(digits))))

def nth_flip(K):
    start_pow = int(math.floor(math.log(K, BASE)))
    digits = []
    for p in range(start_pow, -1, -1):
        d = K / (BASE ** p)
        digits.append(d)
        K %= BASE ** p
    unflipped = [FLIPABLE[d] for d in digits]
    return flip(unflipped)

def main():
    for K in sys.stdin.readlines():
        print nth_flip(int(K))

if __name__ == '__main__':
    main()

