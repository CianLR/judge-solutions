N = int(input())

smear_len = 0
real_len = 0
for _ in range(N):
    m, s = map(int, input().split())
    smear_len += m
    real_len += s / 60

d = real_len / smear_len
print(d if d > 1 else 'measurement error')


