
class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def get_value(self):
        if not self.children:
            return sum(self.metadata)
        s = 0
        for m in self.metadata:
            if 1 <= m <= len(self.children):
                s += self.children[m - 1].get_value()
        return s

def parse_tree(codes, i=0):
    c, m = codes[i], codes[i + 1]
    i += 2
    children = []
    for _ in xrange(c):
        child, i = parse_tree(codes, i)
        children.append(child)
    metadata = []
    for _ in xrange(m):
        metadata.append(codes[i])
        i += 1
    return Node(children, metadata), i

def main():
    codes = [int(x) for x in raw_input().split()]
    tree, _ = parse_tree(codes)
    print tree.get_value()

if __name__ == '__main__':
    main()

