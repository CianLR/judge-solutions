xs = []
ys = []
for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

new_x = min(xs, key=lambda x: xs.count(x))
new_y = min(ys, key=lambda y: ys.count(y))
print(new_x, new_y)
