from math import factorial

def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def binomial(tot, wins, win_chance):
    return choose(tot, wins) * (win_chance ** wins) * ((1 - win_chance) ** (tot - wins))

def take_bet(S, R, X, Y, W):
    success_roll = (S - R + 1.0) / S
    tot_chance = 0
    for succ_needed in range(X, Y + 1):
        tot_chance += binomial(Y, succ_needed, success_roll)
    expected_result = tot_chance * W
    return expected_result > 1

def main():
    N = int(raw_input())
    for _ in range(N):
        R, S, X, Y, W = (int(x) for x in raw_input().split())
        print "yes" if take_bet(S, R, X, Y, W) else "no"

if __name__ == '__main__':
    main()

