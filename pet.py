grades = [(i, sum(map(int, input().split()))) for i in range(1, 6)]
print(*max(grades, key=lambda x:x[1]))
