from collections import deque

EPS = 1e-9

class Line:
    def __init__(self, p1, p2):
        self.a = p2[1] - p1[1]
        self.b = p1[0] - p2[0]
        self.c = (self.a * p1[0]) + (self.b * p1[1])
        self.x_start, self.x_end = sorted([p1[0], p2[0]])
        self.y_start, self.y_end = sorted([p1[1], p2[1]])
        self.p1 = p1
        self.p2 = p2

    def intersects(self, other):
        det = (other.b * self.a) - (self.b * other.a)
        if det == 0:
            return (self.p1 == other.p1 or self.p1 == other.p2 or
                    self.p2 == other.p1 or self.p2 == other.p2)
        x = ((other.b * self.c) - (self.b * other.c)) / det
        y = ((self.a * other.c) - (other.a * self.c)) / det
        return (
            max(self.x_start, other.x_start) - EPS <= x <= EPS + min(self.x_end, other.x_end) and
            max(self.y_start, other.y_start) - EPS <= y <= EPS + min(self.y_end, other.y_end))

def build_graph(P, pipes, well_id):
    adj = [[] for _ in xrange(P)]
    for i in xrange(P):
        for j in xrange(i + 1, P):
            if well_id[i] != well_id[j] and pipes[i].intersects(pipes[j]):
                adj[i].append(j)
                adj[j].append(i)
    return adj

def check_bipartite(P, adj):
    colour = [None] * P
    for start in xrange(P):
        if colour[start] is not None:
            continue
        colour[start] = True
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if colour[v] == colour[u]:
                    return False
                elif colour[v] is not None:
                    continue
                colour[v] = not colour[u]
                q.append(v)
    return True

def main():
    W, P = (int(x) for x in raw_input().split())
    wells = [tuple(int(x) for x in raw_input().split()) for _ in xrange(W)]
    pipe_well_id = []
    pipes = []
    for _ in xrange(P):
        s, x, y = (int(x) for x in raw_input().split())
        pipe_well_id.append(s - 1)
        pipes.append(Line(wells[s - 1], (x, y)))
    adj = build_graph(P, pipes, pipe_well_id)
    print("possible" if check_bipartite(P, adj) else "impossible")

if __name__ == '__main__':
    main()

