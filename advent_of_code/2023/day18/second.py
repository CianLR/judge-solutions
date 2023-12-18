import sys, heapq
from collections import namedtuple, defaultdict

UP    = (-1,  0)
DOWN  = ( 1,  0)
LEFT  = ( 0, -1)
RIGHT = ( 0,  1)
DIREC_TO_TUP = {"3": UP, "1": DOWN, "2": LEFT, "0": RIGHT}

def vec_add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

def vec_mul(v1, m):
  return (v1[0] * m, v1[1] * m)

Command = namedtuple('Command', ['direc', 'direc_vec', 'dist', 'color'])

def get_verts(cmds):
  verts = [(0, 0)]
  perim = 0
  for cmd in cmds:
    vec = vec_mul(cmd.direc_vec, cmd.dist)
    perim += cmd.dist
    nxt_vert = vec_add(verts[-1], vec)
    verts.append(nxt_vert)
  return verts, perim

def area(verts):
    segs = segments(verts)
    area = 0
    for ((x0, y0), (x1, y1)) in segs:
      area += x0*y1 - x1*y0
    return abs(area) // 2

def segments(p):
    return zip(p, p[1:] + [p[0]])

def parse_command(line):
  _, _, col = line.split()
  dst, d = col[2:7], col[7]
  return Command(d, DIREC_TO_TUP[d], int(dst, 16), col)

def main():
  sys.setrecursionlimit(100000)
  cmds = [parse_command(line) for line in sys.stdin.read().split('\n')]
  verts, perim = get_verts(cmds)
  a = area(verts)
  print(a + (perim // 2) + 1)


if __name__ == '__main__':
  main()