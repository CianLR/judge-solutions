
class Node:
    def __init__(self, i, neighbours):
        self.i = i
        self.nbrs = set(neighbours)

N = int(input())
while N != -1:
    nodes = []
    for i in range(N):
        neighbours = [j for j, a in enumerate(input().split()) if a == '1']
        nodes.append(Node(i, neighbours))

    strong = [False]*N
    for node in nodes:
        for n_i in node.nbrs:
            if node.nbrs & nodes[n_i].nbrs:
                strong[node.i] = True
                break

    print(*[i for i, st in enumerate(strong) if not st])

    N = int(input())

