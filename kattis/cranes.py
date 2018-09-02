
EPS = 1e-6

def touching(a, b):
    (x1, y1, r1), (x2, y2, r2) = a, b
    return (x1 - x2)**2 + (y1 - y2)**2 <= (r1 + r2) ** 2

def recur_take(N, cranes, touchgrid, crane_i=0, taken=()):
    if crane_i == N:
        return 0
    for j in taken:
        if touchgrid[crane_i][j]:
            return recur_take(N, cranes, touchgrid, crane_i + 1, taken)
    take_area = cranes[crane_i][2] ** 2
    return max(
            recur_take(N, cranes, touchgrid, crane_i + 1, taken),
            recur_take(N, cranes, touchgrid, crane_i + 1, taken + (crane_i,)) + take_area)



def max_area(N, cranes):
    touchgrid = [[False] * N for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(i, N):
            if touching(cranes[i], cranes[j]):
                touchgrid[i][j] = True
                touchgrid[j][i] = True
    return recur_take(N, cranes, touchgrid)

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        cranes = [tuple(map(int, raw_input().split())) for _ in xrange(N)]
        print max_area(N, cranes)

if __name__ == '__main__':
    main()

