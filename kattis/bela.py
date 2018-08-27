
def get_val(val, suit, dom_suit):
    return {
        'A': (11, 11),
        'K': (4, 4),
        'Q': (3, 3),
        'J': (2, 20),
        'T': (10, 10),
        '9': (0, 14),
        '8': (0, 0),
        '7': (0, 0),
    }[val][suit == dom_suit]

N, B = input().split()
N = int(N) * 4
tot_points = 0
for _ in range(N):
    tot_points += get_val(*input(), B)

print(tot_points)
