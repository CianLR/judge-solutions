from collections import defaultdict, deque

class Node:
    def __init__(self):
        self.adj = set()

def bfs_has_cycle(start, seen):
    q = deque([(start, None)])
    seen.add(start)
    while q:
        u, p = q.popleft()
        for v in u.adj:
            if v in seen:
                if v is not p:
                    return True
                continue
            q.append((v, u))
            seen.add(v)
    return False

def graph_has_cycle(graph):
    seen = set()
    for u in graph.values():
        if u not in seen and bfs_has_cycle(u, seen):
            return True
    return False

def main():
    K = int(raw_input())
    space_nodes = defaultdict(Node)
    floor_nodes = defaultdict(Node)
    for _ in xrange(K):
        x1, y1, z1, x2, y2, z2 = (int(x) for x in raw_input().split())
        space1, space2 = (x1, y1, z1), (x2, y2, z2)
        space_nodes[space1].adj.add(space_nodes[space2])
        space_nodes[space2].adj.add(space_nodes[space1])
        floor1, floor2 = space1[:2], space2[:2]
        if floor1 == floor2:
            continue
        floor_nodes[floor1].adj.add(floor_nodes[floor2])
        floor_nodes[floor2].adj.add(floor_nodes[floor1])

    if graph_has_cycle(space_nodes):
        print "True closed chains"
    else:
        print "No true closed chains"

    if graph_has_cycle(floor_nodes):
        print "Floor closed chains"
    else:
        print "No floor closed chains"

if __name__ == '__main__':
    main()

