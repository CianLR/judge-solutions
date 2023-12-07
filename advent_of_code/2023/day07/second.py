import sys
from collections import Counter, namedtuple

RANK_ORDER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]

Hand = namedtuple('Hand', ['cards', 'bid', 'htype'])

def get_card_rank(c):
    return RANK_ORDER.index(c)
  
def determine_type(cards):
  cgroup = Counter(cards)
  if 'J' in cgroup and cgroup['J'] < 5:
    jcount = cgroup['J']
    del cgroup['J']
    high_card = max(cgroup, key=lambda k: cgroup[k])
    cgroup[high_card] += jcount
  ccount = tuple(sorted(cgroup.values()))
  if ccount == (5,):
    return 6
  elif ccount == (1, 4):
    return 5
  elif ccount == (2, 3):
    return 4
  elif ccount == (1, 1, 3):
    return 3
  elif ccount == (1, 2, 2):
    return 2
  elif ccount == (1, 1, 1, 2):
    return 1
  return 0

def parse_hand(line):
  cards, bid = line.split()
  bid = int(bid)
  return Hand(cards, bid, determine_type(cards))

def hand_to_comp(h):
  return (h.htype, *(get_card_rank(c) for c in h.cards))

def get_winnings(hands):
  hands = sorted(hands, key=hand_to_comp)
  winnings = 0
  for rank, hand in zip(range(1, len(hands) + 1), hands):
    winnings += rank * hand.bid
  return winnings
  
def main():
  lines = sys.stdin.read().split('\n')
  hands = []
  for l in lines:
    h = parse_hand(l)
    hands.append(h)
  print(get_winnings(hands))
  
if __name__ == '__main__':
  main()