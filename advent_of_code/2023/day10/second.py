import sys
from collections import defaultdict

ADJ = {
  '|': ((1, 0), (-1, 0)),
  '-': ((0, -1), (0, 1)),
  'L': ((1, 0), (0, 1)),
  'J': ((1, 0), (0, -1)),
  '7': ((-1, 0), (0, -1)),
  'F': ((-1, 0), (0, 1)),
  '.': (),
  'S': (),
}

def within_bounds(grid, r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[r])

def get_start(grid):
  for r, cols in enumerate(grid):
    for c, point in enumerate(cols):
      if point == 'S':
        return (r, c)

def build_adj(grid):
  adj = defaultdict(set)
  for r, line in enumerate(grid):
    for c, v in enumerate(line):
      for rm, cm in ADJ[v]:
        nr, nc = r + rm, c + cm
        if within_bounds(grid, nr, nc):
          adj[(r, c)].add((nr, nc))
          if grid[nr][nc] == 'S':
            adj[(nr, nc)].add((r, c))
  return adj

def get_loop(grid):
  adj = build_adj(grid)
  start = get_start(grid)
  loop = []
  prev = None
  u = start
  while not len(loop) or u != start:
    for v in adj[u]:
      if v != prev:
        loop.append(v)
        prev, u = u, v
        break
  return loop

def print_grid(g):
  for l in g[::-1]:
    print(''.join(list(l)))

def bfs(grid, lset, seen, sr, sc):
  seen.add((sr, sc))
  stack = [(sr, sc)]
  while stack:
    r, c = stack.pop()
    for np in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
      if within_bounds(grid, np[0], np[1]) and np not in lset and np not in seen:
        stack.append(np)
        seen.add(np)
        grid[np[0]][np[1]] = 'x'

def floodfill(grid, loop):
  seen = set()
  lset = set(loop)
  # Vert sides
  for r in range(len(grid)):
    for c in (0, len(grid[r])-1):
      if (r, c) not in lset and (r, c) not in seen:
        bfs(grid, lset, seen, r, c)
  # Horz sides
  for r in (0, len(grid) - 1):
    for c in range(len(grid[r])):
      if (r, c) not in lset and (r, c) not in seen:
        bfs(grid, lset, seen, r, c)
  return seen

def get_enclosed(grid):
  loop = get_loop(grid)
  egrid = []
  for l in grid:
    egrid.append(['.'] * len(l) * 2)
    egrid.append(['.'] * len(l) * 2)
  print_grid(grid)
  extened_loop = []
  prevr, prevc = loop[-1]
  for lr, lc in loop:
    if prevr != lr:
      egrid[prevr + lr][prevc + lc] = '|'
    else:
      egrid[prevr + lr][prevc + lc] = '-'
    egrid[lr * 2][lc * 2] = grid[lr][lc]
    extened_loop.append((prevr + lr, prevc + lc))
    extened_loop.append((lr * 2, lc * 2))
    prevr, prevc = lr, lc
  print_grid(egrid)

  out_points = floodfill(egrid, extened_loop)
  real_out_points = sum(r % 2 == 0 and c % 2 == 0 for r, c in out_points)
  grid_size = len(grid) * len(grid[0])
  loop_size = len(loop)
  print_grid(egrid)
  print(f"{grid_size=} {loop_size=} {real_out_points=}")
  return grid_size - loop_size - real_out_points


def main():
  lines = [x.strip() for x in sys.stdin.readlines()][::-1]
  print(get_enclosed(lines))

if __name__ == '__main__':
  main()