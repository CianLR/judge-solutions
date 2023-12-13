import sys
from collections import defaultdict

def get_verts(grid):
  reflections = set(range(1, len(grid[0])))
  for row in grid:
    next_ref = reflections.copy()
    for mid in reflections:
      l = mid - 1
      r = mid
      while 0 <= l < len(row) and 0 <= r < len(row):
        if row[l] != row[r]:
          next_ref.remove(mid)
          break
        l, r = l - 1, r + 1
    reflections = next_ref
  return reflections
      


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