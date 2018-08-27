class Node:
    def __init__(self, name):
        self.name = name
        self.connected = []
        self.color = None


def main():
    N = int(input())
    items = [input() for _ in range(N)]
    nodes = {name: Node(name) for name in items}
    
    M = int(input())
    for _ in range(M):
        a, b = input().split()
        nodes[a].connected.append(nodes[b])
        nodes[b].connected.append(nodes[a])
    
    walt, jessie = [], []
    stack = []
    seen = set()
    for name in items:
        if name in seen:
            continue
        nodes[name].color = True
        stack.append(nodes[name])
        while stack:
            n = stack.pop()
            if n.name in seen:
                continue
            seen.add(n.name)
            if n.color:
                walt.append(n.name)
            else:
                jessie.append(n.name)
            for nbr in n.connected:
                if nbr.color is None:
                    nbr.color = not n.color
                    stack.append(nbr)
                elif nbr.color == n.color:
                    print("impossible")
                    return
    print(' '.join(walt))
    print(' '.join(jessie))


if __name__ == '__main__':
    main()

