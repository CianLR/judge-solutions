# from queue import Queue

# class UnionFind:
#     def __init__(self):
#         self.weights = {}
#         self.parents = {}

#     def __getitem__(self, node):
#         if node not in self.parents:
#             self.parents[node] = node
#             self.weights[node] = 1
#             return node

#         path = [node]
#         root = self.parents[node]
#         while root != path[-1]:
#             path.append(root)
#             root = self.parents[root]

#         # Path compression
#         for ancestor in path:
#             self.parents[ancestor] = root
#         return root

#     def join(self, *nodes):
#         roots = [self[x] for x in nodes]
#         heaviest = max(roots, key=lambda r: self.weights[r])
#         for r in roots:
#             if r != heaviest:
#                 self.weights[heaviest] += self.weights[r]
#                 self.parents[r] = heaviest

# class Node:
#     def __init__(self, r, c, val):
#         self.r = r
#         self.c = c
#         self.val = val

def counter():
    i = 0
    while True:
        yield i
        i += 1

R, C = map(int, raw_input().split())
# uf = UnionFind()
type_grid = [[None]*C for _ in range(R)]
for r in range(R):
    l = raw_input()
    for c in range(C):
        type_grid[r][c] = l[c]

col_grid = [[None]*C for _ in range(R)]
count = counter()
for r in range(R):
    for c in range(C):
        if col_grid[r][c] is not None:
            continue

        fill = type_grid[r][c]
        colour = next(count)
        q = [(r, c)]
        while q:
            r, c = q.pop()
            if col_grid[r][c] is not None:
                continue
            col_grid[r][c] = colour

            if r + 1 < R and col_grid[r+1][c] is None and type_grid[r+1][c] == fill:
                q.append((r+1, c))
            if r - 1 >= 0 and col_grid[r-1][c] is None and type_grid[r-1][c] == fill:
                q.append((r-1, c))
            if c + 1 < C and col_grid[r][c+1] is None and type_grid[r][c+1] == fill:
                q.append((r, c+1))
            if c - 1 >= 0 and col_grid[r][c-1] is None and type_grid[r][c-1] == fill:
                q.append((r, c-1))


# for r in range(R):
#     l = input()
#     for c in range(C):
#         grid[r][c] = Node(r, c, l[c])
#         connects = [grid[r][c]]
#         if r > 0 and grid[r-1][c].val == grid[r][c].val:
#             connects.append(grid[r-1][c])
#         if c > 0 and grid[r][c-1].val == grid[r][c].val:
#             connects.append(grid[r][c-1])
#         uf.join(*connects)
# print()
# for r in range(R):
#     for c in range(C):
#         print(col_grid[r][c], end='')
#     print()
N = int(raw_input())
for _ in range(N):
    r1, c1, r2, c2 = map(lambda x: int(x) - 1, raw_input().split())
    if col_grid[r1][c1] != col_grid[r2][c2]:
        print('neither')
    else:
        print('decimal' if type_grid[r1][c1] == '1' else 'binary')
