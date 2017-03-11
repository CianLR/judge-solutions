T = int(input())
for _ in range(T):
    N = int(input())
    print(len(set([input() for _ in range(N)])))
