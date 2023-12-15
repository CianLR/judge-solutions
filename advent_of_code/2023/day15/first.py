import sys
from collections import defaultdict

def HASH(s):
  v = 0
  for c in s:
    v = ((ord(c) + v) * 17) % 256
  return v


def main():
  seq = input().split(',')
  v = 0
  for part in seq:
    v += HASH(part)
  print(v)

if __name__ == '__main__':
  main()