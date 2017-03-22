d1 = list(map(int, input()))
d2 = list(map(int, input()))

if len(d1) > len(d2):
    d2 = [0]*(len(d1) - len(d2)) + d2
elif len(d2) > len(d1):
    d1 = [0]*(len(d2) - len(d1)) + d1

nd1 = ''
nd2 = ''
for a, b in zip(d1, d2):
    if a > b:
        nd1 += str(a)
    elif b > a:
        nd2 += str(b)
    else:
        nd1 += str(a)
        nd2 += str(b)
print(int(nd1) if nd1 else 'YODA')
print(int(nd2) if nd2 else 'YODA')
