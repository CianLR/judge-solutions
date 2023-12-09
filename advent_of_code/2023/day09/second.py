import sys
from collections import Counter, namedtuple

def all_zero(seq):
  return all(x == 0 for x in seq)

def diff(seq):
  return [a - b for a, b in zip(seq[1:], seq[:-1])]

def next_val(seq):
  stack = [seq]
  while not all_zero(stack[-1]):
    stack.append(diff(stack[-1]))
  # for s in stack: print(s)
  for i, s in enumerate(stack):
    stack[i] = s[::-1]
  for hi, lo in zip(stack[:0:-1], stack[-2::-1]):
    lo.append(lo[-1] - hi[-1])
  # for s in stack: print(s)
  return stack[0][-1]


def main():
  lines = sys.stdin.read().split('\n')
  hist = 0
  for l in lines:
    readings = [int(x) for x in l.strip().split()]
    hist += next_val(readings)
  print(hist)
  
if __name__ == '__main__':
  main()