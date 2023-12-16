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

def dfs(grid, pos, direc, _seen=set()):
  if (pos, direc) in _seen:
    return _seen
  if not within_grid(grid, *pos):
    return _seen
  _seen.add((pos, direc))
  r, c = pos
  if grid[r][c] == '.':
    dfs(grid, vec_add(pos, direc), direc)
  elif grid[r][c] == '/':
    nd = FWSLASH[direc]
    dfs(grid, vec_add(pos, nd), nd)
  elif grid[r][c] == '\\':
    nd = BKSLASH[direc]
    dfs(grid, vec_add(pos, nd), nd)
  elif grid[r][c] == '-':
    if direc in (LEFT, RIGHT):
      dfs(grid, vec_add(pos, direc), direc)
    else:
      dfs(grid, vec_add(pos, RIGHT), RIGHT)
      dfs(grid, vec_add(pos, LEFT), LEFT)
  elif grid[r][c] == '|':
    if direc in (UP, DOWN):
      dfs(grid, vec_add(pos, direc), direc)
    else:
      dfs(grid, vec_add(pos, UP), UP)
      dfs(grid, vec_add(pos, DOWN), DOWN)
  return _seen

def main():
  sys.setrecursionlimit(100000)
  grid = sys.stdin.read().split('\n')
  seen = dfs(grid, (0, 0), RIGHT)
  print(len({p for p, d in seen}))

if __name__ == '__main__':
  main()