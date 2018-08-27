from math import log, floor
from bisect import bisect_right

LARGE = 4194305
#LARGE = 10

def bits_needed(k):
    return floor(k) + 1

def year_to_bits(y):
    y = (y / 10) - 194
    return 2 ** y

def main():
    fact_bits = [0]
    f = 1
    while fact_bits[-1] < LARGE:
        fact_bits.append(fact_bits[-1] + log(f, 2))
        f += 1
    
    Y = int(raw_input())
    while Y != 0:
        bits = year_to_bits(Y)
        print bisect_right(fact_bits, bits) - 1
        Y = int(raw_input())


if __name__ == '__main__':
    main()

