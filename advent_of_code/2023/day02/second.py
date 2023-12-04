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

def power(game):
  r, g, b = 0, 0, 0
  for round in game.rounds:
    r, g, b = max(r, round.red), max(g, round.green), max(b, round.blue)
  return r * g * b

def main():
  lines = sys.stdin.readlines()
  ans = 0
  for l in lines:
    game = parse_line(l.strip())
    ans += power(game)
  print(ans)

if __name__ == '__main__':
  main()