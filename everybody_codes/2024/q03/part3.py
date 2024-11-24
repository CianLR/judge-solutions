import sys

def adj(levels, x, y):
  for xm in range(x-1, x+2):
    for ym in range(y-1, y+2):
      if 0 <= xm < len(levels[y]) and 0 <= ym < len(levels):
        yield (xm, ym)
      else:
        yield (-1, -1)

def do_dig(levels, digs):
  dug = 0
  new_digs = []
  for x, y in digs:
    l = levels[y][x]
    for ax, ay in adj(levels, x, y):
      adj_l = 0
      if (ax, ay) != (-1, -1):
        adj_l = levels[ay][ax]
      if adj_l - l > 0:
        break
    else:
      levels[y][x] -= 1
      dug += 1
      new_digs.append((x, y))
  return dug, new_digs

def main():
  map = sys.stdin.readlines()
  digs = []
  for y, line in enumerate(map):
    for x, c in enumerate(line):
      if c == '#':
        digs.append((x, y))
  levels = [[0] * len(line) for line in map]
  total_dug = 0
  while True:
    dug, digs = do_dig(levels, digs)
    total_dug += dug
    if dug == 0:
      break
  print(total_dug)

main()