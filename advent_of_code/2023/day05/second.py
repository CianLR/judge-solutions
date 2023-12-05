import sys
from collections import namedtuple

class RangeMap:
  def __init__(self):
    self.ranges = []
  
  def add_range(self, dst, src, rlen):
    self.ranges.append((src, dst, rlen))
  
  def __getitem__(self, src):
    for s, d, l in self.ranges:
      if s <= src < s + l:
        return d + (src - s)
    return src
  
  def pack(self, m=99999999999):
    final_ranges = []
    rs = sorted(self.ranges)
    ri = 0
    s = 0
    while s < m:
      if ri == len(rs):
        final_ranges.append((s, s, m - s))
      elif s < rs[ri][0]:
        final_ranges.append((s, s, rs[ri][0] - s))
      elif s == rs[ri][0]:
        final_ranges.append(rs[ri])
        ri += 1
      else:
        print(s)
        assert False
      s = final_ranges[-1][0] + final_ranges[-1][2]
    self.ranges = final_ranges
  
  def lookup_range(self, src, ln):
    new_ranges = []
    cur_s = src
    for s, d, l in self.ranges:
      if s + l <= cur_s:
        continue
      elif src + ln <= s:
        continue
      starti = cur_s - s
      run_len = min(src + ln, s + l) - cur_s
      new_ranges.append((d + starti, run_len))
      cur_s += run_len
    return new_ranges


  
def parse_map(lines):
  m = RangeMap()
  for line in lines:
    dest, source, rlen = [int(x) for x in line.split()]
    m.add_range(dest, source, rlen)
  m.pack()
  return m

def min_location(ttt, maps, starts):
  curtype = 'seed'
  values = starts
  nextvalues = []
  while curtype != 'location':
    cm = maps[curtype]
    for s, l in values:
      nextvalues.extend(cm.lookup_range(s, l))
    values = nextvalues
    nextvalues = []
    curtype = ttt[curtype]
  return min(values)[0]
  
def main():
  inp = sys.stdin.read()
  inital, *chunks = inp.split('\n\n')
  seedvals = [int(x) for x in inital.split()[1:]]
  seeds = list(zip(seedvals[::2], seedvals[1::2]))
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