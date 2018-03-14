
def best_gain(money, max_shares, prices):
    shares_owned = min(money // prices[0], max_shares)
    money -= shares_owned * prices[0]
    for i in range(len(prices) - 1):
        if prices[i + 1] < prices[i]:
            money += prices[i] * shares_owned
            shares_owned = min(max_shares, money // prices[i + 1])
            money -= shares_owned * prices[i + 1]
    return money + (shares_owned * prices[-1])

def main():
    N = int(input())
    prices = [int(input()) for _ in range(N)]
    print(best_gain(100, 100000, prices))

if __name__ == '__main__':
    main()

