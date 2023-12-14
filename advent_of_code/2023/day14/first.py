import sys
from collections import defaultdict

def tilt_north(grid):
  grid = list(map(list, zip(*grid)))
  ng = []
  for col in grid:
    take = 0
    c = []
    while take < len(col):
      if col[take] == '.':
        pass
      elif col[take] == 'O':
        c.append('O')
      else:
        c.extend(['.'] * (take - len(c)))
        c.append(col[take])
      take += 1
    c.extend(['.'] * (len(col) - len(c)))
    ng.append(c)
  return list(map(list, zip(*ng)))

def calc_load(grid):
  load = 0
  for i, row in enumerate(grid):
    load += (len(grid) - i) * row.count('O')
  return load
  
def main():
  grid = [x.strip() for x in sys.stdin.readlines()]
  grid2 = tilt_north(grid)
  print(calc_load(grid2))

if __name__ == '__main__':
  main()