import sys
from collections import defaultdict

def run_sub_one(runs):
  x, *rest = runs
  if x == 1:
    return tuple(rest), True
  return tuple([x-1] + rest), False



def count_matches(memo, p, pi, runs, last_run_end=False, last_hash=False):
  # print(f"count_matches({''.join(pattern)}, {runs}, {last_run_end=}, {last_hash=})")
  if len(p) == pi or len(runs) == 0:
    return int(all(p in '?.' for p in p[pi:]) and len(runs) == 0)
  m = (pi, runs, last_run_end, last_hash)
  if m in memo:
    return memo[m]
  c = p[pi]
  if c == '#':
    if last_run_end:
      return 0
    ret = count_matches(memo, p, pi + 1, *run_sub_one(runs), True)
    memo[m] = ret
    return ret
  if c == '.':
    if not last_run_end and last_hash:
      return 0
    ret = count_matches(memo, p, pi + 1, runs, False, False)
    memo[m] = ret
    return ret
  # pattern 0 is ?
  matches = 0
  if not last_hash or not last_run_end:
    matches += count_matches(memo, p, pi + 1, *run_sub_one(runs), True)
  if last_run_end or not last_hash:
    matches += count_matches(memo, p, pi + 1, runs, False, False)
  memo[m] = matches
  return matches

def unfold(patten, runs):
  return '?'.join([patten] * 5), (*runs, *runs, *runs, *runs, *runs)

def main():
  lines = [x.split() for x in sys.stdin.readlines()]
  matches = 0
  for pattern, runs in lines:
    runs = tuple(int(x) for x in runs.split(','))
    pattern, runs = unfold(pattern, runs)
    m = count_matches({}, pattern, 0, runs)
    # print(pattern, runs, m)
    matches += m
  print(matches)

if __name__ == '__main__':
  main()