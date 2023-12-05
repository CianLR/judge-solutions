import sys
from collections import namedtuple

class RangeMap:
  def __init__(self):
    self.ranges = []
  
  def add_range(self, dst, src, rlen):
    self.ranges.append((dst, src, rlen))
  
  def __getitem__(self, src):
    for d, s, l in self.ranges:
      if s <= src < s + l:
        return d + (src - s)
    return src
  
def parse_map(lines):
  m = RangeMap()
  for line in lines:
    dest, source, rlen = [int(x) for x in line.split()]
    m.add_range(dest, source, rlen)
  return m

def min_location(ttt, maps, starts):
  curtype = 'seed'
  values = starts
  nextvalues = []
  while curtype != 'location':
    cm = maps[curtype]
    for v in values:
      nextvalues.append(cm[v])
    values = nextvalues
    nextvalues = []
    curtype = ttt[curtype]
  return min(values)
  
def main():
  inp = sys.stdin.read()
  inital, *chunks = inp.split('\n\n')
  seeds = [int(x) for x in inital.split()[1:]]
  type_to_type = {}
  maps = {}
  for chunk in chunks:
    lines = chunk.split('\n')
    src, _, dst = lines[0].split()[0].split('-')
    type_to_type[src] = dst
    maps[src] = parse_map(lines[1:])
  print(min_location(type_to_type, maps, seeds))

if __name__ == '__main__':
  main()