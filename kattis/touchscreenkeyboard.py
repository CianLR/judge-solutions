
coords = {}
kb = [
  "qwertyuiop",
  "asdfghjkl",
  "zxcvbnm"]
for i, l in enumerate(kb):
    for j, c in enumerate(l):
        coords[c] = (i, j)

def get_dist(w1, w2):
    diff = 0
    for c1, c2 in zip(w1, w2):
        x1, y1 = coords[c1]
        x2, y2 = coords[c2]
        diff += abs(x1 - x2) + abs(y1 - y2)
    return diff

N = int(input())
for _ in range(N):
    W, M = input().split()
    words = []
    for _ in range(int(M)):
        new_w = input()
        words.append((get_dist(W, new_w), new_w))
    for d, w in sorted(words):
        print(w, d)
