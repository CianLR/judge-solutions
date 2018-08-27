K = int(input())

a = 1
b = 0
for _ in range(K):
    a, b = b, a + b

print(a, b)
