import heapq
from collections import deque

def get_start_end_trees(H, W, grid):
    start = end = None
    trees = []
    for h in xrange(H):
        for w in xrange(W):
            if grid[h][w] == '.':
                continue
            elif grid[h][w] == '+':
                trees.append((h, w))
            elif grid[h][w] == 'V':
                start = (h, w)
            elif grid[h][w] == 'J':
                end = (h, w)
    return start, end, trees

def adj(H, W, h, w):
    for hm, wm in ((h + 1, w), (h, w + 1), (h - 1, w), (h, w - 1)):
        if 0 <= hm < H and 0 <= wm < W:
            yield hm, wm

def bfs_cost(H, W, grid, trees):
    queue = deque([(0, h, w) for h, w in trees])
    cost_grid = [[None] * W for _ in xrange(H)]
    for h, w in trees:
        cost_grid[h][w] = 0
    while queue:
        d, h, w = queue.popleft()
        for hm, wm in adj(H, W, h, w):
            if cost_grid[hm][wm] is not None:
                continue
            cost_grid[hm][wm] = d + 1
            queue.append((d + 1, hm, wm))
    return cost_grid

def dijkstra(H, W, start, end, grid):
    sh, sw = start
    pq = [(-grid[sh][sw], sh, sw)]
    dist_grid = [[1] * W for _ in xrange(H)]
    while pq:
        d, h, w = heapq.heappop(pq)
        if dist_grid[h][w] < d:
            continue
        if (h, w) == end:
            return -d
        for hm, wm in adj(H, W, h, w):
            new_d = max(d, -grid[hm][wm])
            if dist_grid[hm][wm] <= new_d:
                continue
            dist_grid[hm][wm] = new_d
            heapq.heappush(pq, (new_d, hm, wm))
    assert False

def main():
    H, W = [int(x) for x in raw_input().split()]
    grid = [raw_input() for _ in xrange(H)]
    start, end, trees = get_start_end_trees(H, W, grid)
    cost_grid = bfs_cost(H, W, grid, trees)
    print dijkstra(H, W, start, end, cost_grid)

if __name__ == '__main__':
    main()

