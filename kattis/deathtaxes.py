import sys

class Holdings:
    def __init__(self):
        self.shares = 0
        self.cost = 0
        self.death_takings = None

    def buy(self, n, c):
        tot = self.shares + n
        self.cost = ((self.shares * self.cost) + (n * c)) / tot
        self.shares = tot

    def sell(self, n, c):
        self.shares -= n

    def split(self, n):
        self.shares *= n
        self.cost /= n

    def merge(self, n):
        self.shares //= n
        self.cost *= n

    def die(self, c):
        profit = max(c - self.cost, 0)
        self.death_takings = self.shares * (c - (profit * 0.3))

def main():
    holds = Holdings()
    events = {
        'buy': holds.buy,
        'sell': holds.sell,
        'split': holds.split,
        'merge': holds.merge,
        'die': holds.die,
    }
    for cmd in sys.stdin.readlines():
        c, *args = cmd.split()
        events[c](*map(int, args))
    print(holds.death_takings)

if __name__ == '__main__':
    main()

