from collections import deque

DIRS = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

def step(p, d):
    return p[0] + DIRS[d][0], p[1] + DIRS[d][1]

class Node:
    def __init__(self, loc):
        self.loc = loc
        self.adj = []

    def add_adj(self, oth):
        self.adj.append(oth)

def draw_graph(direcs):
    curr = (0, 0)
    nodes = {curr: Node(curr)}
    for d in direcs:
        nxt = step(curr, d)
        if nxt not in nodes:
            nodes[nxt] = Node(nxt)
        nodes[nxt].add_adj(nodes[curr])
        nodes[curr].add_adj(nodes[nxt])
        curr = nxt
    return nodes[(0, 0)], nodes[curr]

def bfs(start, end):
    q = deque([(0, start)])
    seen = set()
    while q:
        d, u = q.pop()
        if u is end:
            return d
        for v in u.adj:
            if v in seen:
                continue
            seen.add(v)
            q.appendleft((d + 1, v))

def main():
    N = int(input())
    for _ in range(N):
        input()
        K = int(input())
        direcs = [input() for _ in range(K)]
        start, end = draw_graph(direcs)
        print(bfs(start, end))

if __name__ == '__main__':
    main()

