
def sieve_of_erat(N):
    grid = [True] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if not grid[i]:
            continue
        primes.append(i)
        for j in range(i * 2, N + 1, i):
            grid[j] = False
    return primes

PRIMES = sieve_of_erat(1000)

def factor_n(n):
    for p in PRIMES:
        if n % p == 0:
            return p, n // p

def extended_euclidean(totient, e):
    original_totient = totient
    x,y, u,v = 0,1, 1,0
    while totient != 0:
        q, r = e // totient, e % totient
        m, n = x - u * q, y - v * q
        e, totient, x,y, u,v = totient,r, u,v, m,n
    return y if y > 0 else y + original_totient

def find_d(n, e):
    p, q = factor_n(n)
    tot = (p - 1) * (q - 1)
    return extended_euclidean(tot, e)

def main():
    T = int(input())
    for _ in range(T):
        n, e = map(int, input().split())
        print(find_d(n, e))


if __name__ == '__main__':
    main()

