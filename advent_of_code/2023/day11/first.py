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
  # Empty rows
  egrid = []
  for r, cols in enumerate(grid):
    empty = True
    for c, point in enumerate(cols):
      empty = empty and point != '#'
    egrid.append(cols)
    if empty:
      egrid.append(cols)
  
  egrid2 = [[] for _ in range(len(egrid))]
  for c in range(len(egrid[0])):
    empty = True
    for r in range(len(egrid)):
      empty = empty and egrid[r][c] != '#'
    for r in range(len(egrid)):
      egrid2[r].append(egrid[r][c])
      if empty:
        egrid2[r].append(egrid[r][c])
  return egrid2


def sum_shortest_paths(stars):
  path_sum = 0
  for i, (r1, c1) in enumerate(stars):
    for (r2, c2) in stars[i+1:]:
      path_sum += abs(r1 - r2) + abs(c1 - c2)
  return path_sum


def main():
  lines = [x.strip() for x in sys.stdin.readlines()][::-1]
  egrid = expand_grid(lines)
  stars = find_stars(egrid)
  print(sum_shortest_paths(stars))
  # for l in egrid[::-1]:
  #   print(''.join(l))

if __name__ == '__main__':
  main()