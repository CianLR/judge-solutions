import sys, heapq
from collections import namedtuple, defaultdict, deque

Point = namedtuple('Point', ['x', 'y', 'z'])

def iterate_block(start, end):
  for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
    for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
      for z in range(min(start.z, end.z), max(start.z, end.z) + 1):
        yield Point(x, y, z)

def stack_bricks(bricks):
  bricks = sorted(bricks, key=lambda s: min(s[0].z, s[1].z))
  final_bricks = []
  max_heights = defaultdict(int)
  for start, end in bricks:
    final_height = 0
    for cube in iterate_block(start, end):
      final_height = max(final_height, max_heights[(cube.x, cube.y)] + 1)
    fall_dist = min(start.z, end.z) - final_height
    final_bricks.append((
      Point(start.x, start.y, start.z - fall_dist),
      Point(end.x, end.y, end.z - fall_dist),
    ))
    for cube in iterate_block(final_bricks[-1][0], final_bricks[-1][1]):
      if cube.z > max_heights[(cube.x, cube.y)]:
        max_heights[(cube.x, cube.y)] = cube.z
  return final_bricks

def get_supported(bricks):
  grid = {}
  for i, (s, e) in enumerate(bricks):
    for cube in iterate_block(s, e):
      grid[cube] = i
  supports = [set() for _ in range(len(bricks))]
  supported_by = [set() for _ in range(len(bricks))]
  for i, (s, e) in enumerate(bricks):
    for cube in iterate_block(s, e):
      below = grid.get((cube.x, cube.y, cube.z - 1), i)
      if below != i:
        supported_by[i].add(below)
        supports[below].add(i)
  return supports, supported_by

def find_safe(bricks, supported_by):
  safe = {i for i in range(len(bricks))}
  for supports in supported_by:
    if len(supports) == 1:
      s = tuple(supports)[0]
      if s in safe:
        safe.remove(s)
  return safe


def display_profile(bricks, cmp=0):
  print(' ' + str(cmp))
  print('012')
  for z in range(9, -1, -1):
    for c in range(0, 3):
      cs = set()
      for i, (s, e) in enumerate(bricks):
        for cube in iterate_block(s, e):
          if cube[cmp] == c and cube.z == z:
            cs.add(i)
      if not cs:
        print('.',end='')
      elif len(cs) == 1:
        print(chr(list(cs)[0] + ord('A')), end='')
      else:
        print('?', end='')
    print(' ' + str(z))

def falls_dfs(supports, supported_by, brick, deleted):
  deleted.add(brick)
  for sup in supports[brick]:
    for dep in supported_by[sup]:
      if dep not in deleted:
        break
    else:
      falls_dfs(supports, supported_by, sup, deleted)

def find_falls(bricks, supports, supported_by):
  all_falls = 0
  for i in range(len(bricks)):
    deleted = set()
    falls_dfs(supports, supported_by, i, deleted)
    all_falls += len(deleted) - 1
  return all_falls

def main():
  sys.setrecursionlimit(100000)
  bricks = []
  for line in sys.stdin.read().split('\n'):
    a, b = line.split('~')
    bricks.append((
      Point(*map(int, a.split(','))),
      Point(*map(int, b.split(','))),
    ))
  stacked = stack_bricks(bricks)
  supports, supported_by = get_supported(stacked)
  falls = find_falls(bricks, supports, supported_by)
  print(falls)

if __name__ == '__main__':
  main()