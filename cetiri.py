a, b, c = sorted(map(int, input().split()))
if c - b == b - a:
    print(c + (c - b))
elif c - b > b - a:
    print(b + (b - a))
else:
    print(a + (c - b))
