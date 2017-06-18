T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    prizes = []
    for _ in range(N):
        n, *indexes, money = map(int, input().split())
        prizes.append((indexes, money))
    
    collection = [0] + [int(x) for x in input().split()]
    tot_money = 0
    for inds, money in prizes:
        fin = False
        while not fin:
            for i in inds:
                if not collection[i]:
                    fin = True
                    break
                collection[i] -= 1
            if not fin:
                tot_money += money
    print(tot_money)

