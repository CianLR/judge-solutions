
def max_profit(listeners, price):
    best_profit = 0
    cur_cost = 0
    cur_listens = 0
    for l in listeners:
        cur_cost += price
        cur_listens += l
        best_profit = max(best_profit, cur_listens - cur_cost)
        if cur_cost > cur_listens:
            cur_listens = 0
            cur_cost = 0
    return best_profit

def main():
    N, P = map(int, input().split())
    listeners = [int(x) for x in input().split()]
    print(max_profit(listeners, P))

if __name__ == '__main__':
    main()

