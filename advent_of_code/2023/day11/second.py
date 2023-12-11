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

def find_stars(grid):
  stars = []
  for r, line in enumerate(grid):
    for c, v in enumerate(line):
      if v == '#':
        stars.append((r, c))
  return stars
  
def expand_grid(grid):
  empty_rows = set()
  for r, cols in enumerate(grid):
    empty = True
    for c, point in enumerate(cols):
      empty = empty and point != '#'
    if empty:
      empty_rows.add(r)
  
  empty_cols = set()
  for c in range(len(grid[0])):
    empty = True
    for r in range(len(grid)):
      empty = empty and grid[r][c] != '#'
    if empty:
      empty_cols.add(c)
  return empty_rows, empty_cols


def sum_shortest_paths(stars, em_rows, em_cols):
  empty_mul = 1000000
  path_sum = 0
  for i, (r1, c1) in enumerate(stars):
    for (r2, c2) in stars[i+1:]:
      for r in range(min(r1, r2), max(r1, r2)):
        path_sum += empty_mul if r in em_rows else 1
      for c in range(min(c1, c2), max(c1, c2)):
        path_sum += empty_mul if c in em_cols else 1
  return path_sum


def main():
  grid = [x.strip() for x in sys.stdin.readlines()][::-1]
  em_rows, em_cols = expand_grid(grid)
  stars = find_stars(grid)
  print(sum_shortest_paths(stars, em_rows, em_cols))
  # for l in egrid[::-1]:
  #   print(''.join(l))

if __name__ == '__main__':
  main()