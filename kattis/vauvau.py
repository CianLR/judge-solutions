a_aggr, a_calm, b_aggr, b_calm = map(int, input().split())
a_tot = a_aggr + a_calm
b_tot = b_aggr + b_calm
arrivals = map(lambda x: int(x) - 1, input().split())

for ar in arrivals:
    dog_a_cycle = ar % a_tot
    dog_b_cycle = ar % b_tot

    dog_a_calm = dog_a_cycle >= a_aggr
    dog_b_calm = dog_b_cycle >= b_aggr

    if dog_a_calm and dog_b_calm:
        print("none")
    elif dog_b_calm or dog_a_calm:
        print("one")
    else:
        print("both")
