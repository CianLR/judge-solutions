
W = int(raw_input())
N = int(raw_input())
area = 0
for _ in range(N):
    a, b = raw_input().split()
    area += int(a) * int(b)
print(area / W)

