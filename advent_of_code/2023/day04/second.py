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


def card_matches(card):
  value = 0
  for x in card.have:
    if x in card.win:
      value += 1
  return value

def dfs(cards, cid, _memo={}):
  if cid in _memo:
    return _memo[cid]
  matches = card_matches(cards[cid])
  c = sum(dfs(cards, c) for c in range(cid + 1, cid + matches + 1)) + 1
  _memo[cid] = c
  return c
  
def main():
  lines = [l.strip() for l in sys.stdin.readlines()]
  cards = []
  for l in lines:
    cards.append(parse_card(l))
  print(sum(dfs(cards, c) for c in range(len(cards))))

if __name__ == '__main__':
  main()