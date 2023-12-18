import sys, heapq
from collections import namedtuple, defaultdict

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)
DIREC_TO_TUP = {"U": UP, "D": DOWN, "L": LEFT, "R": RIGHT}

def vec_add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

Command = namedtuple('Command', ['direc', 'direc_vec', 'dist', 'color'])

def dig_grid(cmds):
  grid = {(0, 0)}
  curr = (0, 0)
  for cmd in cmds:
    for _ in range(cmd.dist):
      curr = vec_add(curr, cmd.direc_vec)
      grid.add(curr)
  return grid

def parse_command(line):
  d, dst, col = line.split()
  return Command(d, DIREC_TO_TUP[d], int(dst), col)

def print_grid(grid):
  min_r = min(x[0] for x in grid)
  max_r = max(x[0] for x in grid)
  min_c = min(x[1] for x in grid)
  max_c = max(x[1] for x in grid)
  for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
      print('#' if (r, c) in grid else '.', end='')
    print()

Bounds = namedtuple('Bounds', ['min_r', 'max_r', 'min_c', 'max_c'])

def within_bounds(b, p):
  return b.min_r <= p[0] < b.max_r and b.min_c <= p[1] < b.max_c

def dfs(grid, bounds, start):
  seen = {start}
  stack = [start]
  inside = True
  while stack:
    curr = stack.pop()
    for d in DIREC_TO_TUP.values():
      nxt = vec_add(curr, d)
      if nxt in grid or nxt in seen:
        continue
      if not within_bounds(bounds, nxt):
        inside = False
        continue
      stack.append(nxt)
      seen.add(nxt)
  return inside, seen

def count_inside(grid):
  min_r = min(x[0] for x in grid)
  max_r = max(x[0] for x in grid)
  min_c = min(x[1] for x in grid)
  max_c = max(x[1] for x in grid)
  b = Bounds(min_r, max_r + 1, min_c, max_c + 1)
  all_seen = set()
  inside = set()
  for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
      if (r, c) in grid or (r, c) in all_seen:
        continue
      ins, s = dfs(grid, b, (r, c))
      if ins:
        inside.update(s)
      all_seen.update(s)
  return len(inside) + len(grid)

def main():
  sys.setrecursionlimit(100000)
  cmds = [parse_command(line) for line in sys.stdin.read().split('\n')]
  grid = dig_grid(cmds)
  print(count_inside(grid))


if __name__ == '__main__':
  main()