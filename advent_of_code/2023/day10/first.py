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

def loop_len(grid):
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
  return len(loop)

def main():
  lines = [x.strip() for x in sys.stdin.readlines()][::-1]
  print(loop_len(lines) // 2)

if __name__ == '__main__':
  main()