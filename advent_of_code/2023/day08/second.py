import sys
from collections import defaultdict
from itertools import cycle
from functools import reduce

def parse_line(l):
  n, _, l, r = l.strip().split()
  return n, l[1:-1], r[:-1]

def gcd(a, b):
  return b if a == 0 else gcd(b % a, a)

def lcm(a, b):
  return (a * b) // gcd(a, b)

def lcm_seq(seq):
  return reduce(lcm, seq)

def apply_instrs(instrs, nodes):
  z_steps = []
  for n in (n for n in nodes if n.endswith('A')):
    for step, inst in enumerate(cycle(instrs)):
      if n.endswith('Z'):
        z_steps.append(step)
        break
      n = nodes[n][inst]
  return lcm_seq(z_steps)

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
