
N = int(input())
for _ in range(N):
    K, *gnomes = map(int, input().split())
    for i in range(1, K - 1):
        if gnomes[i - 1] + 1 != gnomes[i]:
            print(i + 1)
            break

