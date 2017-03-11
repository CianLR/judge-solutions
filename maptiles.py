quad = list(map(int, input()))

zoom_level = len(quad)

# 2**n
coords = [(0, 0), (1, 0),
          (0, 1), (1, 1)]
x_y = [0, 0]
for q in quad:
    # Scale the coords thing
    x_y = [p * 2 for p in x_y]
    # Add the new offset
    x_y = [p + mod for p, mod in zip(x_y, coords[q])]

print(zoom_level, *x_y)
