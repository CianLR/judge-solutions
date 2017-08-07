
class Player:
    def __init__(self):
        self.won = 0
        self.lost = 0

    def get_avg(self):
        if not self.won and not self.lost:
            return '-'
        win_ratio = self.won / float(self.won + self.lost)
        return '{:.3f}'.format(round(win_ratio, 3))

games = {
    'rock': {
        'rock': 0,
        'paper': -1,
        'scissors': 1,
    },
    'paper': {
        'rock': 1,
        'paper': 0,
        'scissors': -1,
    },
    'scissors': {
        'rock': -1,
        'paper': 1,
        'scissors': 0,
    },    
}

def get_won(a, b):
    return games[a][b]


def get_num_games(n, k):
    return k * ((n * (n - 1)) // 2)

def main():
    meta = raw_input()
    while meta != '0':
        N, K = (int(x) for x in meta.split())
        players = [None] + [Player() for _ in range(N)]
        for _ in range(get_num_games(N, K)):
            p1, t1, p2, t2 = raw_input().split()
            w = get_won(t1, t2)
            if w == 1:
                players[int(p1)].won += 1
                players[int(p2)].lost += 1
            elif w == -1:
                players[int(p2)].won += 1
                players[int(p1)].lost += 1

        for p in players[1:]:
            print p.get_avg()
        print ''

        meta = raw_input()

if __name__ == '__main__':
    main()

