from queue import Queue

def note_to_coord(n):
    return ord(n[0]) - ord('a'), ord(n[1]) - ord('1')

def coord_to_note(c):
    return 'abcdefgh'[c[0]] + str(c[1] + 1)

def on_board(p):
    return 0 <= p[0] <= 7 and 0 <= p[1] <= 7

def next_moves(p):
    muts = [
        (1, 2), (2, 1), (2, -1), (1, -2),
        (-1, -2), (-2, -1), (-2, 1), (-1, 2)
    ]
    for m in muts:
        np = p[0] + m[0], p[1] + m[1]
        if on_board(np):
            yield np

def order(lst):
    return sorted(
        sorted(
            lst,
            key=lambda p: p[0]),
        key=lambda p: p[1],
        reverse=True)

T = int(input())
for _ in range(T):
    knight_start = note_to_coord(input())
    dists = {}
    q = Queue()
    # Co-ord, dist
    q.put((knight_start, 0))
    while not q.empty():
        p, dist = q.get()
        dists[p] = dist
        for np in next_moves(p):
            if np not in dists:
                q.put((np, dist + 1))

    furthest_val = max(dists.values())
    furthest = [coord_to_note(p) for p in dists if dists[p] == furthest_val]

    print(furthest_val, *order(furthest))
