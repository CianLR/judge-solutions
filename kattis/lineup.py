N = int(input())
p = [input() for _ in range(N)]

s_p = sorted(p)
if p == s_p:
    print('INCREASING')
elif p == s_p[::-1]:
    print('DECREASING')
else:
    print('NEITHER')
