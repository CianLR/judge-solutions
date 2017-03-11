from itertools import permutations
from math import ceil

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(ceil(n**0.5))+1):
        if n%i == 0:
            return False
    return True

def dig_from_it(it):
    d = 0
    for i in it:
        d = (d*10) + i
    return d

C = int(input())
for _ in range(C):
    t = list(map(int, input()))
    seen = set()
    primes = 0
    for l in range(len(t)):
        for tc in permutations(t, l):
            if tc in seen:
                continue
            if is_prime(dig_from_it(tc)):
                print(dig_from_it(tc))
                primes += 1
    print(primes)
