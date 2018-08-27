from sys import stdin
import heapq

def adj(H, W, u):
    h, w = u
    for nh, nw in ((h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)):
        if 0 <= nh < H and 0 <= nw < W:
            yield nh, nw

def dijkstra(H, W, grid):
    start = (0, 0)
    end = (H - 1, W - 1)
    pq = [(0, grid[0][0], start)]
    ladder = {}
    while pq:
        lad, curh, u = heapq.heappop(pq)
        if u in ladder and ladder[u] < lad:
            continue
        if u == end:
            return lad
        for v in adj(H, W, u):
            h = grid[v[0]][v[1]]
            new_lad = max(lad, h - curh)
            if v in ladder and ladder[v] <= new_lad:
                continue
            ladder[v] = new_lad
            heapq.heappush(pq, (new_lad, h, v))

def main():
    H, W = [int(x) for x in stdin.readline().split()]
    grid = [[int(x) for x in stdin.readline().split()] for _ in xrange(H)]
    print dijkstra(H, W, grid)

if __name__ == '__main__':
    main()

