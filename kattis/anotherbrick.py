import sys

h, w, n = map(int, input().split())
bricks = list(map(int, input().split()))

curr_wall = 0
for b in bricks:
    curr_wall += b
    if curr_wall == w:
        curr_wall = 0
        h -= 1
    elif curr_wall > w:
        print("NO")
        sys.exit()

    if h == 0:
        print("YES")
        sys.exit()

print("NO")
