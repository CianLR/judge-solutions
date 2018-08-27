N = int(input())
trees = sorted(map(int, input().split()), reverse=True)

max_day = 0
for i, tree in enumerate(trees):
    max_day = max(max_day, i + tree + 2)
print(max_day)
