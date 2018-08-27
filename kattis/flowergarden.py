from bisect import bisect_right

def sieve(N):
    grid = [True] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if not grid[i]:
            continue
        primes.append(i)
        for j in range(i * 2, N + 1, i):
            grid[j] = False
    return primes

PRIMES = sieve(20000)

def largest_prime_le(n):
    return PRIMES[bisect_right(PRIMES, n) - 1]

def point_dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def water_flowers(max_dist, flowers):
    curr_pos = (0, 0)
    curr_dist = 0
    flowers_watered = 0
    for f in flowers:
        curr_dist += point_dist(f, curr_pos)
        if curr_dist > max_dist:
            break
        curr_pos = f
        flowers_watered += 1
    return largest_prime_le(flowers_watered) if flowers_watered > 1 else 0
    

def main():
    T = int(input())
    for _ in range(T):
        N, D = map(int, input().split())
        flowers = []
        for _ in range(N):
            x, y = map(int, input().split())
            flowers.append((x, y))
        print(water_flowers(D, flowers))



if __name__ == '__main__':
    main()

