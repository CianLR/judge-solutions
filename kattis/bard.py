N = int(input())
E = int(input())

v = [set() for _ in range(N)]
tot_songs = 0
for _ in range(E):
    K, *vils = map(lambda i: int(i) - 1, input().split())
    if 0 in vils:
        for vil in vils:
            v[vil].add(tot_songs)
        tot_songs += 1
    else:
        tot_knowl = set()
        for vil in vils:
            tot_knowl.update(v[vil])
        for vil in vils:
            v[vil].update(tot_knowl)

for vil, songs in enumerate(v): 
    if len(songs) == tot_songs:
        print(vil + 1)

