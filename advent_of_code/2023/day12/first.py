import sys
from collections import defaultdict

def run_sub_one(runs):
  x, *rest = runs
  if x == 1:
    return tuple(rest), True
  return tuple([x-1] + rest), False



def count_matches(pattern, runs, last_run_end=False, last_hash=False):
  # print(f"count_matches({''.join(pattern)}, {runs}, {last_run_end=}, {last_hash=})")
  if len(pattern) == 0 or len(runs) == 0:
    return int(all(p in '?.' for p in pattern) and len(runs) == 0)
  c, *rest = pattern
  if c == '#':
    return 0 if last_run_end else count_matches(rest, *run_sub_one(runs), True)
  if c == '.':
    if not last_run_end and last_hash:
      return 0
    return count_matches(rest, runs, False, False)
  # pattern 0 is ?
  matches = 0
  if not last_hash or not last_run_end:
    matches += count_matches(rest, *run_sub_one(runs), True)
  if last_run_end or not last_hash:
    matches += count_matches(rest, runs, False, False)
  return matches


def main():
  lines = [x.split() for x in sys.stdin.readlines()]
  matches = 0
  for pattern, runs in lines:
    runs = tuple(int(x) for x in runs.split(','))
    m = count_matches(pattern, runs)
    # print(pattern, runs, m)
    matches += m
  print(matches)

if __name__ == '__main__':
  main()