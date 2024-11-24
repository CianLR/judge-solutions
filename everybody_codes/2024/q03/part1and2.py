import sys

def adj(levels, x, y):
  if x > 0: yield (x - 1, y)
  if y > 0: yield (x, y - 1)
  if y + 1 < len(levels): yield (x, y + 1)
  if x + 1 < len(levels[y]): yield (x + 1, y)

def do_dig(levels, digs):
  dug = 0
  new_digs = []
  for x, y in digs:
    l = levels[y][x]
    for ax, ay in adj(levels, x, y):
      if levels[ay][ax] - l > 0:
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