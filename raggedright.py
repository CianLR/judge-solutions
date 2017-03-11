import sys

lines = sys.stdin.readlines()
n = max([len(l) for  l in lines])
score = 0
for l in lines[:-1]:
    score += (n - len(l))**2

print(score)
