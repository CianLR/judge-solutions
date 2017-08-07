
r_from = [
    (0,),
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (2, 3, 5, 6, 8, 9, 0),
    (3, 6, 9),
    (4, 5, 6, 7, 8, 9, 0),
    (5, 6, 8, 9, 0),
    (6, 9),
    (7, 8, 9, 0),
    (8, 9, 0),
    (9,),
]

# 1 digit
possible = list(range(10))
# 2 digits
for first in range(10):
    possible += [(first * 10) + x for x in r_from[first]]
# 3 digits
possible.append(200)
for first in range(2):
    for second in r_from[first]:
        possible += [(first * 100) + (second * 10) + x for x in r_from[second]]

N = int(input())
for _ in range(N):
    k = int(input())
    print(min(possible, key=lambda x: abs(k - x)))

