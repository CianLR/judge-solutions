import sys
from collections import defaultdict

def adj(r, c):
  for rm, cm in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
    yield r + rm, c + cm

def walk_grid(grid):
  gearadj = defaultdict(list)
  for r in range(len(grid)):
    part = ''
    gears = set()
    for c in range(len(grid[r])):
      v = grid[r][c]
      if not v.isdigit():
        if part:
          for g in gears:
            gearadj[g].append(int(part))
        gears = set()
        part = ''
        continue
      part += v
      for r2, c2 in adj(r, c):
        if 0 <= r2 < len(grid) and 0 <= c2 < len(grid[r2]):
          if grid[r2][c2] == '*':
            gears.add((r2, c2))
    if part:
      for g in gears:
        gearadj[g].append(int(part))
  ans = 0
  for vals in gearadj.values():
    if len(vals) == 2:
      ans += vals[0] * vals[1]
  return ans


def main():
  lines = [l.strip() for l in sys.stdin.readlines()]
  ans = walk_grid(lines)
  print(ans)

if __name__ == '__main__':
  main()