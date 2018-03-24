from collections import deque

LEFT, DOWN, RIGHT, UP = 1, 2, 4, 8

def get_openings(H, W, maze):
    opens = []
    for w in range(W):
        if not maze[0][w] & UP:
            opens.append((0, w))
        if not maze[H - 1][w] & DOWN:
            opens.append((H - 1, w))
    for h in range(H):
        if not maze[h][0] & LEFT:
            opens.append((h, 0))
        if not maze[h][W - 1] & RIGHT:
            opens.append((h, W - 1))
    return opens

def adj(H, W, p, v):
    h, w = p
    if 0 <= h - 1 and not v & UP:
        yield h - 1, w
    if h + 1 < H and not v & DOWN:
        yield h + 1, w
    if 0 <= w - 1 and not v & LEFT:
        yield h, w - 1
    if w + 1 < W and not v & RIGHT:
        yield h, w + 1

def bfs(H, W, maze, start):
    q = deque([(start, None)])
    seen = set([start])
    multipath = False
    while q:
        u, p = q.popleft()
        for v in adj(H, W, u, maze[u[0]][u[1]]):
            if v in seen:
                if v != p:
                    multipath = True
                continue
            seen.add(v)
            q.append((v, u))
    return multipath, seen

def check_valid(H, W, maze):
    start, end = get_openings(H, W, maze)
    multipath, seen = bfs(H, W, maze, start)
    if end not in seen:
        return "NO SOLUTION"
    elif len(seen) != H * W:
        return "UNREACHABLE CELL"
    elif multipath:
        return "MULTIPLE PATHS"
    return "MAZE OK"

def main():
    H, W = [int(x) for x in input().split()]
    while H or W:
        maze = [[int(c, 16) for c in input()] for _ in range(H)]
        print(check_valid(H, W, maze))
        H, W = [int(x) for x in input().split()]


if __name__ == '__main__':
    main()

