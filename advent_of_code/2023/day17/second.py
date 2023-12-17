import sys, heapq
from collections import namedtuple

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)

def valid_moves(direc, straights):
  if straights < 9:
    yield direc
  if straights < 3:
    return  # We force a straight
  yield from {
    UP: (LEFT, RIGHT),
    DOWN: (LEFT, RIGHT),
    LEFT: (UP, DOWN),
    RIGHT: (UP, DOWN)
  }[direc]

def within_grid(grid, r, c):
  return 0 <= r < len(grid) and 0 <= c < len(grid[r])

def vec_add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

Node = namedtuple('Node', ['dist', 'point', 'direc', 'straights'])

def dijkstra(grid):
  end = (len(grid) - 1, len(grid[0]) - 1)
  q = [Node(0, (0, 0), RIGHT, 0)]
  seen = set()
  while q:
    u = heapq.heappop(q)
    if u.straights >= 3 and u.point == end:
      return u.dist
    for new_direc in valid_moves(u.direc, u.straights):
      new_point = vec_add(u.point, new_direc)
      if not within_grid(grid, *new_point):
        continue
      new_dist = u.dist + grid[new_point[0]][new_point[1]]
      new_straights = u.straights + 1 if u.direc == new_direc else 0
      seen_key = (new_point, new_direc, new_straights)
      if seen_key in seen:
        continue
      seen.add(seen_key)
      heapq.heappush(q, Node(new_dist, new_point, new_direc, new_straights))
  return -1


def main():
  sys.setrecursionlimit(100000)
  grid = [[int(x) for x in line] for line in sys.stdin.read().split('\n')]
  dist = dijkstra(grid)
  print(dist)

if __name__ == '__main__':
  main()