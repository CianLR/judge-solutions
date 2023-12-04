import sys

def adj(r, c):
  for rm, cm in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
    yield r + rm, c + cm

def walk_grid(grid):
  parts = []
  for r in range(len(grid)):
    part = ''
    is_adj = False
    for c in range(len(grid[r])):
      v = grid[r][c]
      if not v.isdigit():
        if part and is_adj:
          parts.append(int(part))
        part = ''
        is_adj = False
        continue
      part += v
      for r2, c2 in adj(r, c):
        if 0 <= r2 < len(grid) and 0 <= c2 < len(grid[r2]):
          v2 = grid[r2][c2]
          if not v2.isdigit() and v2 != '.':
            is_adj = True
    if part and is_adj:
      parts.append(int(part))
  return sum(parts)


def main():
  lines = [l.strip() for l in sys.stdin.readlines()]
  ans = walk_grid(lines)
  print(ans)

if __name__ == '__main__':
  main()