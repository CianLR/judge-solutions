
class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

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

def sum_metadata(tree):
    return sum(tree.metadata) + sum(map(sum_metadata, tree.children))

def main():
    codes = [int(x) for x in raw_input().split()]
    tree, _ = parse_tree(codes)
    print sum_metadata(tree)

if __name__ == '__main__':
    main()

