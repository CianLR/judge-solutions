class Branch:
    def __init__(self, i):
        self.i = i
        self.root_i = None

    def add_root(self, root_i):
        self.root_i = root_i

K = int(input())
branches = {}

l = input()
while l != '-1':
    a, *bs = map(int, l.split())

    if a not in branches:
        branches[a] = Branch(a)

    for b_i in bs:
        if b_i not in branches:
            branches[b_i] = Branch(b_i)
        branches[b_i].add_root(a)

    l = input()

path = [K]
cur_branch = branches[K]
while cur_branch.root_i is not None:
    cur_branch = branches[cur_branch.root_i]
    path.append(cur_branch.i)

print(*path)
