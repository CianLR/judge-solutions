import sys
from collections import namedtuple

Card = namedtuple('Card', ['cid', 'win', 'have'])

def parse_card(line):
  cid, rest = line[len('Card '):].split(': ')
  win, have = rest.split(' | ')
  return Card(
    cid,
    {int(x) for x in win.split()},
    {int(x) for x in have.split()})


def card_value(card):
  value = 0
  for x in card.have:
    if x in card.win:
      if value == 0:
        value = 1
      else:
        value *= 2
  return value

  
def main():
  lines = [l.strip() for l in sys.stdin.readlines()]
  ans = 0
  for l in lines:
    card = parse_card(l)
    ans += card_value(card)
  print(ans)

if __name__ == '__main__':
  main()