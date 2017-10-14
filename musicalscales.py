
alln = 'A A# B C C# D D# E F F# G G#'.split()
scale_step = [2, 2, 1, 2, 2, 2, 1]

scales = {}
for i in range(len(alln)):
    n = [alln[i]]
    for m in scale_step:
        i = (i + m) % len(alln)
        n.append(alln[i])
    scales[n[0]] = set(n)

N = int(input())
notes = set(input().split())

used = set()
for name, sc in scales.items():
    if sc.issuperset(notes):
        used.add(name)

order = []
for n in alln:
    if n in used:
        order.append(n)

if order:
    print(*order)
else:
    print("none")

