N, M = map(int, input().split())

outcomes = {}
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i + j in outcomes:
            outcomes[i + j] += 1
        else:
            outcomes[i + j] = 1

highest_outcome = max(outcomes.values())
highest_sums = filter(lambda k: outcomes[k] == highest_outcome, outcomes)
for s in sorted(highest_sums):
    print(s)    
