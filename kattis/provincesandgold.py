
BUY_POWER = [3, 2, 1]
TREASURE = [
    ("Gold", 6),
    ("Silver", 3),
    ("Copper", 0),
]
VICTORY = [
    ("Province", 8),
    ("Duchy", 5),
    ("Estate", 2),
]

def main():
    coins = [int(x) for x in input().split()]
    value = sum(a * b for a, b in zip(coins, BUY_POWER))
    buys = []
    for v, c in VICTORY:
        if c <= value:
            buys.append(v)
            break
    for t, c in TREASURE:
        if c <= value:
            buys.append(t)
            break
    print(' or '.join(buys))


if __name__ == '__main__':
    main()

