import sys
from collections import namedtuple, defaultdict

Round = namedtuple('Round', ['red', 'blue', 'green'])
Game = namedtuple('Game', ['gid', 'rounds'])

def parse_round(r):
  balls = r.split(', ')
  colors = defaultdict(int)
  for b in balls:
    amt, color = b.split()
    colors[color] = int(amt)
  return Round(colors['red'], colors['blue'], colors['green'])

def parse_line(l):
  gid, rest = l[len("Game "):].split(': ')
  return Game(int(gid), [parse_round(r) for r in rest.split('; ')])

def is_valid(game):
  for r in game.rounds:
    if r.red > 12 or r.green > 13 or r.blue > 14:
      return False
  return True

def main():
  lines = sys.stdin.readlines()
  ans = 0
  for l in lines:
    game = parse_line(l.strip())
    if is_valid(game):
      ans += game.gid
  print(ans)

if __name__ == '__main__':
  main()