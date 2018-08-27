
N = int(input())
for _ in range(N):
    b, p = input().split()
    b = int(b)
    p = float(p)
    
    calc = (60 * b) / p
    mini = (60 * (b - 1)) / p
    maxi = (60 * (b + 1)) / p
    print(mini, calc, maxi)

