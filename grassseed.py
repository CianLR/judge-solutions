C = float(input())
L = int(input())
total_cost = 0
for _ in range(L):
    w, h = map(float, input().split())
    total_cost += w * h * C

print(total_cost)
