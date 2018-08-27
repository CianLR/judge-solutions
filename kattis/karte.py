import sys

card_string = input()
cards = {
    'P': set(),
    'K': set(),
    'H': set(),
    'T': set(),
}

for i in range(len(card_string)//3):
    card = card_string[i*3:(i+1)*3]
    suit, val = card[0], card[1:]
    if val in cards[suit]:
        print("GRESKA")
        sys.exit()

    cards[suit].add(val)

print(*[13 - len(cards[s]) for s in ['P', 'K', 'H', 'T']])
