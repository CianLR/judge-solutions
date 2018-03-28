
T = int(input())
for _ in range(T):
    N = int(input())
    perf = sorted((int(x) for x in input().split()), reverse=True)
    print(sum(perf[(i * 2) + 1] for i in range(N)))

