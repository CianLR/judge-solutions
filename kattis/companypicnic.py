from collections import defaultdict

class Node:
    def __init__(self):
        self.i = -1
        self.speed = None
        self.parent = None
        self.children = []

def combine_averages(avgs):
    count = 0
    speed_sum = 0.0
    for c, a in avgs:
        count += c
        speed_sum += c * a
    return count, (speed_sum / count) if count else 0.0

MEMO = {}

def get_best_pairs(root, can_use_parent=True):
    if not root.children:
        return 0, 0.0
    if (root.i, can_use_parent) in MEMO:
        return MEMO[(root.i, can_use_parent)]
    best = combine_averages([get_best_pairs(c) for c in root.children])
    if not can_use_parent:
        return best
    for i, c in enumerate(root.children):
        avgs = (
            [(1, min(root.speed, c.speed))] +
            [get_best_pairs(v, j != i) for j, v in enumerate(root.children)])
        best = max(best, combine_averages(avgs))
    MEMO[(root.i, can_use_parent)] = best
    return best

def main():
    node_name = defaultdict(Node)
    nodes = []
    N = int(raw_input())
    for i in xrange(N):
        name, speed, par_name = raw_input().split()
        node_name[name].i = i
        node_name[name].parent = node_name[par_name]
        node_name[par_name].children.append(node_name[name])
        node_name[name].speed = float(speed)
    c, a = get_best_pairs(node_name['CEO'].children[0])
    print c, a

if __name__ == '__main__':
    main()
