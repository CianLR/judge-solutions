import sys
from collections import namedtuple


def opt_window(time, dist):
  beats = 0
  for t in range(time):
    d = t * (time - t)
    if d > dist:
      beats += 1
  return beats


def main():
  t = int(''.join(input().split()[1:]))
  d = int(''.join(input().split()[1:]))
  print(opt_window(t, d))

if __name__ == '__main__':
  main()