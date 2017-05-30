N = int(input())
probs = sorted([float(input().split()[1]) for _ in range(N)], reverse=True)
expected = 0
for i, prob in enumerate(probs):
    expected += (i + 1) * prob
print(expected)
