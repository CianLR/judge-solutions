
def sieve(N, K):
    grid = [True] * (N + 1)
    crossed = 1
    for p in range(2, N + 1):
        if not grid[p]:
            continue
        if crossed == K:
            return p
        crossed += 1
        for np in range(2 * p, N + 1, p):
            if not grid[np]:
                continue
            if crossed == K:
                return np
            grid[np] = False
            crossed += 1
    raise Exception("Hello")

def main():
    N, K = map(int, input().split())
    print(sieve(N, K))

if __name__ == '__main__':
    main()

