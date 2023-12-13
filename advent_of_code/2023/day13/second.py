import sys
from collections import defaultdict

def get_verts(grid):
  reflections = {x: 0 for x in range(1, len(grid[0]))}
  for row in grid:
    for mid in reflections:
      if reflections[mid] > 1:
        continue
      l = mid - 1
      r = mid
      while 0 <= l < len(row) and 0 <= r < len(row):
        if row[l] != row[r]:
          reflections[mid] += 1
          break
        l, r = l - 1, r + 1
  return [k for k, v in reflections.items() if v == 1]      


def get_horiz(grid):
  return get_verts(list(zip(*grid)))
  
def main():
  patterns = [x.split('\n') for x in sys.stdin.read().split('\n\n')]
  verts = []
  horiz = []
  for grid in patterns:
    verts.extend(get_verts(grid))
    horiz.extend(get_horiz(grid))
  print((sum(horiz) * 100) + sum(verts))

if __name__ == '__main__':
  main()