T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lines = [[int(x) for x in input()] for _ in range(N)]
    out = []
    for i in range(M):
        ones = len([1 for j in range(N) if lines[j][i] == 1])
        if ones > N / 2:
            out.append('1')
        else:
            out.append('0')
    print(''.join(out))
