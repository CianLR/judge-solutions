
class Node:
    def __init__(self, degree, parent=None):
        self.parent = parent
        self.degree_left = degree - (parent is not None)


def main():
    N = int(raw_input())
    degree = [int(x) for x in raw_input().split()]

    nodes = [Node(degree[0])]
    curr = nodes[0]
    for d in degree[1:]:
        while curr is not None and curr.degree_left == 0:
            curr = curr.parent
        if curr is None:
            print "NO"
            return
        curr.degree_left -= 1
        nodes.append(Node(d, curr))
        curr = nodes[-1]

    print "YES" if all(map(lambda n: n.degree_left == 0, nodes)) else "NO"

if __name__ == '__main__':
    main()

