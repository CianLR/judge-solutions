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
  times = [int(x) for x in input().split()[1:]]
  dists = [int(x) for x in input().split()[1:]]
  m = 1
  for t, d in zip(times, dists):
    m *= opt_window(t, d)
  print(m)

if __name__ == '__main__':
  main()