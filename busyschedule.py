
def time_to_tuple(t):
    hm, Z = t.split()
    h, m = hm.split(':')
    h = int(h) % 12
    m = int(m)
    return (0 if Z == 'a.m.' else 1, h, m, t)


N = int(input())
while N != 0:
    times = [time_to_tuple(input()) for _ in range(N)]
    for t in sorted(times):
        print(t[3])
    print()
    N = int(input())
