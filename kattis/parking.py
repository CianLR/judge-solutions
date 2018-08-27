prices = [0, *map(int, input().split())]
trucks = [tuple(map(int, input().split())) for _ in range(3)]
starts = [t[0] for t in trucks]
ends = [t[1] for t in trucks]

price = 0
curr_trucks = 0
for time in range(1, max(ends) + 1):
    curr_trucks += starts.count(time)
    curr_trucks -= ends.count(time)
    price += prices[curr_trucks] * curr_trucks

print(price)
