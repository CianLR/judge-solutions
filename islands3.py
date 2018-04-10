from collections import deque

def bfs_remove_island(H, W, grid, h, w):
    q = deque([(h, w)])
    grid[h][w] = 'W'
    while q:
        h, w = q.popleft()
        for nh, nw in ((h, w + 1), (h + 1, w), (h, w - 1), (h - 1, w)):
            if 0 <= nh < H and 0 <= nw < W and (grid[nh][nw] == 'L' or grid[nh][nw] == 'C'):
                grid[nh][nw] = 'W'
                q.append((nh, nw))

def count_islands(H, W, grid):
    islands = 0
    for h in xrange(H):
        for w in xrange(W):
            if grid[h][w] == 'L':
                islands += 1
                bfs_remove_island(H, W, grid, h, w)
    return islands


def main():
    H, W = [int(x) for x in raw_input().split()]
    grid = [list(raw_input()) for _ in xrange(H)]
    print count_islands(H, W, grid)

if __name__ == '__main__':
    main()

