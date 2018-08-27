from math import pi

CIRCUM = pi * 60
INDEX = {c: i for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ '")}
SPEED = 15  # f/s

def circle_dist(a, b):
    d = min(abs(INDEX[a] - INDEX[b]),
            len(INDEX) - abs(INDEX[a] - INDEX[b]))
    return CIRCUM * (d / len(INDEX))

N = int(input())
for _ in range(N):
    s = input()
    time = len(s)
    for a, b in zip(s, s[1:]):
        time += circle_dist(a, b) / SPEED
    print(time)

