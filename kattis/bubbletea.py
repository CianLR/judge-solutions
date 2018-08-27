
N = int(input())
teas = [int(x) for x in input().split()]
M = int(input())
tops = [int(x) for x in input().split()]

drink_prices = []
for tea in range(N):
    K, *ts = [int(x) for x in input().split()]
    for top in ts:
        drink_prices.append(teas[tea] + tops[top - 1])

X = int(input())
drinks = X // min(drink_prices)
if drinks <= 1:
    print(0)
else:
    print(drinks - 1)

