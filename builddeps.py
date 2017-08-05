from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.deps = set()
        self.req = 0


def main():
    N = int(input())
    nodes = defaultdict(Node)
    for i in range(N):
        name, *deps = input().replace(':', '').split()
        if name not in nodes:
            nodes[name] = Node(name)
        for d in deps:
            if d not in nodes:
                nodes[d] = Node(d)
            nodes[d].deps.add(name)
    
    root = nodes[input()]
    stack = [root]
    direct_deps = set()
    while stack:
        n = stack.pop()
        if n.name in direct_deps:
            continue
        direct_deps.add(n.name)
        for d in n.deps:
            nodes[d].req += 1
            if d not in direct_deps:
                stack.append(nodes[d])
    zeros = [root]
    while zeros:
        n = zeros.pop()
        print(n.name)
        for d in n.deps:
            dn = nodes[d]
            dn.req -= 1
            if dn.req == 0:
                zeros.append(dn)

if __name__ == '__main__':
    main()

