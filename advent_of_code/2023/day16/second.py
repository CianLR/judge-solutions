import sys
from collections import defaultdict

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)

# /
FWSLASH = {
  UP: RIGHT,
  DOWN: LEFT,
  LEFT: DOWN,
  RIGHT: UP,
}

# \
BKSLASH = {
  UP: LEFT,
  DOWN: RIGHT,
  LEFT: UP,
  RIGHT: DOWN,
}

def within_grid(grid, r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[r])

def vec_add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

def dfs(grid, pos, direc, seen):
  if (pos, direc) in seen:
    return seen
  if not within_grid(grid, *pos):
    return seen
  seen.add((pos, direc))
  r, c = pos
  if grid[r][c] == '.':
    dfs(grid, vec_add(pos, direc), direc, seen)
  elif grid[r][c] == '/':
    nd = FWSLASH[direc]
    dfs(grid, vec_add(pos, nd), nd, seen)
  elif grid[r][c] == '\\':
    nd = BKSLASH[direc]
    dfs(grid, vec_add(pos, nd), nd, seen)
  elif grid[r][c] == '-':
    if direc in (LEFT, RIGHT):
      dfs(grid, vec_add(pos, direc), direc, seen)
    else:
      dfs(grid, vec_add(pos, RIGHT), RIGHT, seen)
      dfs(grid, vec_add(pos, LEFT), LEFT, seen)
  elif grid[r][c] == '|':
    if direc in (UP, DOWN):
      dfs(grid, vec_add(pos, direc), direc, seen)
    else:
      dfs(grid, vec_add(pos, UP), UP, seen)
      dfs(grid, vec_add(pos, DOWN), DOWN, seen)
  return seen

def unique_locs(seen):
  return len({p for p, d in seen})

def best_config(grid):
  best = 0
  height = len(grid)
  width = len(grid[0])
  for r in range(height):
    best = max(best, unique_locs(dfs(grid, (r, 0), RIGHT, set())))
    best = max(best, unique_locs(dfs(grid, (r, width - 1), LEFT, set())))
  for c in range(width):
    best = max(best, unique_locs(dfs(grid, (0, c), DOWN, set())))
    best = max(best, unique_locs(dfs(grid, (height - 1, c), UP, set())))
  return best

def main():
  sys.setrecursionlimit(100000)
  grid = sys.stdin.read().split('\n')
  print(best_config(grid))

if __name__ == '__main__':
  main()