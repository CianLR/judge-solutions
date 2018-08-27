
class Roster:
    def __init__(self, players):
        self.play = players

    def rotate(self, old_player):
        new, *self.play = self.play
        self.play.append(old_player)
        return new

class Team:
    def __init__(self, offence, defence, rost):
        self.o = offence
        self.d = defence
        self.arrive_pair = (offence, defence)
        self.rost = rost

    def rotate(self):
        self.o, self.d = self.rost.rotate(self.d), self.o
        self.arrive_pair = (self.d, self.o)

    def swap(self):
        self.o, self.d = self.d, self.o

    def pair(self):
        return self.arrive_pair

class Game:
    def __init__(self, player_list):
        wo, bo, wd, bd, *rest = player_list
        self.roster = Roster(rest)
        self.white = Team(wo, wd, self.roster)
        self.black = Team(bo, bd, self.roster)
    
    def _get_win_lose(self, result):
        if result == 'W':
            return self.white, self.black
        return self.black, self.white

    def get_dynasties(self, results):
        max_dyn = 0
        dyns = []
        curr_streak = 0
        last_win = None
        for r in results:
            win, lose = self._get_win_lose(r)
            if win == last_win:
                curr_streak += 1
            else:
                if curr_streak == max_dyn:
                    dyns.append(lose.pair())
                elif curr_streak > max_dyn:
                    max_dyn = curr_streak
                    dyns = [lose.pair()]
                curr_streak = 1
            win.swap()
            lose.rotate()
            last_win = win

        if curr_streak == max_dyn:
            dyns.append(last_win.pair())
        elif curr_streak > max_dyn:
            dyns = [last_win.pair()]
        return dyns

def main():
    N = int(input())
    players = input().split()
    results = input()
    game = Game(players)
    for a, b in game.get_dynasties(results):
        print(a, b)


if __name__ == '__main__':
    main()

