import heapq

class PQ:
    def __init__(self, q=None):
        self._q = q or []
        heapq.heapify(self._q)

    def push(self, item):
        heapq.heappush(self._q, item)

    def pop(self):
        return heapq.heappop(self._q)

    def empty(self):
        return len(self._q) == 0


class Node:
    def __init__(self, cost, is_exit):
        self.is_exit = is_exit
        self.edges = []
        self.cost = cost

    def add_edge(self, next_node):
        self.edges.append(next_node)


def on_edge(h, w, H, W):
    return h == 0 or h == H - 1 or w == 0 or w == W - 1


def on_grid(h, w, H, W):
    return 0 <= h < H and 0 <= w < W


def make_graph(grid, H, W):
    nodes = {}
    for h in xrange(H):
        for w in xrange(W):
            if grid[h][w] == '#':
                continue
            nodes[(h, w)] = Node(
                    1 if grid[h][w] == 'c' else 0,
                    on_edge(h, w, H, W))
            for mh, mw in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexth, nextw = h + mh, w + mw
                if on_grid(nexth, nextw, H, W) and grid[nexth][nextw] != '#':
                    nodes[(h, w)].add_edge((nexth, nextw))
    return nodes
            

def get_route(grid, H, W, sh, sw):
    graph = make_graph(grid, H, W)
    # Elements (cost, node_cord)
    # node_cord = (h, w)
    pq = PQ([(1, (sh, sw))])
    seen = set([(sh, sw)])
    while not pq.empty():
        cost, n = pq.pop()
        if graph[n].is_exit:
            return cost
        for nxt in graph[n].edges:
            if nxt not in seen:
                pq.push((cost + graph[nxt].cost, nxt))
                seen.add(nxt)
    # No exit?
    assert False


def main():
    H, W = [int(x) for x in raw_input().split()]
    # grid[h][w]
    grid = [list(raw_input()) for _ in xrange(H)]
    # 1-indexed.
    sh, sw = [int(x) for x in raw_input().split()]
    print(get_route(grid, H, W, sh - 1, sw - 1))


if __name__ == '__main__':
    main()

