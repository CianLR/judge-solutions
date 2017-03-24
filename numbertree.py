H, *path = input().split()
H = int(H)
path = ''.join(path)

r_index = 0
for d in path:
    r_index = (2 * r_index) + (d == 'L')

depth = len(path)
laregest_below = (2 ** (H + 1)) - (2 ** (depth + 1))
print(laregest_below + r_index + 1)
