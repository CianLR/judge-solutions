
class Player:
    def __init__(self, choices, name):
        self._ch = choices
        self._i = 0
        self.points = 0
        self.n = name

    def get_next(self, known):
        while self._ch[self._i] in known:
            self._i += 1
        self._i += 1
        return self._ch[self._i - 1]


def is_similar(a, b):
    return a // 2 == b // 2


def get_similar(a):
    return a + (-1 if a % 2 else 1)


def get_winner(N, anto_ch, matt_ch):
    known = set()
    anto = Player(anto_ch, "anto")
    matt = Player(matt_ch, "matt")
    p = [anto, matt]
    current = 0
    while len(known) < 2 * N:
        guess = p[current].get_next(known)
        known.add(guess)
        if get_similar(guess) in known:
            p[current].points += 1
            continue
        guess2 = p[current].get_next(known)
        known.add(guess2)
        if is_similar(guess, guess2):
            p[current].points += 1
            continue
        elif get_similar(guess2) in known:
            # Other guy knows a winning pair
            p[not current].points += 1
        current = not current

    if anto.points == matt.points:
        return -1
    return 0 if anto.points > matt.points else 1


def main():
    N = int(input())
    anto = [int(x) for x in input().split()]
    matt = [int(x) for x in input().split()]
    print(get_winner(N, anto, matt))


if __name__ == '__main__':
    main()

