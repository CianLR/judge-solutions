import sys
from collections import defaultdict
from itertools import cycle

def parse_line(l):
  n, _, l, r = l.strip().split()
  return n, l[1:-1], r[:-1]

def apply_instrs(instrs, nodes):
  n = 'AAA'
  for step, inst in enumerate(cycle(instrs)):
    if n == 'ZZZ':
      return step
    n = nodes[n][inst]

def main():
  instrs = input()
  input()
  nodes = {}
  for line in sys.stdin.readlines():
    n, l, r = parse_line(line)
    nodes[n] = {'L': l, 'R': r}
  print(apply_instrs(instrs, nodes))

if __name__ == '__main__':
  main()