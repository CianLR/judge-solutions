N, K = map(int, input().split())
probs = [(int(x), i) for i, x in enumerate(input().split())]

solved = 0
time = 0
penalty = 0
for t, i in [probs[K]] + sorted([(t, i) for t, i in probs if i != K]):
    if time + t > 300:
        break
    time += t
    solved += 1
    penalty += time

print(solved, penalty)
