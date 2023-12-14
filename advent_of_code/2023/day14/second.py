import sys
from collections import defaultdict

def reverse_row(grid):
  return [r[::-1] for r in grid]

def transpose(grid):
  return [list(r) for r in zip(*grid)]

def tilt_west(grid):
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
  return ng

def tilt_north(grid):
  return transpose(tilt_west(transpose(grid)))

def tilt_east(grid):
  return reverse_row(tilt_west(reverse_row(grid)))

def tilt_south(grid):
  return transpose(reverse_row(
    tilt_west(
      reverse_row(transpose(grid)))))


def run_cycles(grid, n):
  cyc_next = {}
  gh_prev = tuple(map(tuple, grid))
  cyc_stop = None
  for i in range(n):
    grid = tilt_east(tilt_south(tilt_west(tilt_north(grid))))
    gh = tuple(map(tuple, grid))
    cyc_next[gh_prev] = gh
    gh_prev = gh
    if gh in cyc_next:
      cyc_stop = i
      break
  cyc_len = 1
  gh = cyc_next[gh_prev]
  while gh != gh_prev:
    cyc_len += 1
    gh = cyc_next[gh]
  
  left = n - (cyc_stop + 1)
  steps = left % cyc_len
  gh = gh_prev
  for _ in range(steps):
    gh = cyc_next[gh]
  return calc_load(gh)


def calc_load(grid):
  load = 0
  for i, row in enumerate(grid):
    load += (len(grid) - i) * row.count('O')
  return load
  
def main():
  grid = [x.strip() for x in sys.stdin.readlines()]
  print(run_cycles(grid, 1000000000))

if __name__ == '__main__':
  main()