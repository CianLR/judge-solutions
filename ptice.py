N = int(input())
answers = input()

strats = {
    'Adrian': 'ABC',
    'Bruno': 'BABC',
    'Goran': 'CCAABB',
}

points = {}

for lad in strats:
    lad_pts = 0
    for ans, guess in zip(answers, strats[lad]*N):
        lad_pts += ans == guess
    points[lad] = lad_pts

best = max(points.values())
print(best)
for lad in sorted(points):
    if points[lad] == best:
        print(lad)
