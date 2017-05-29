
T, L, S = map(int, input().split())

max_large = T // L

vol_from_large = L * max_large
while vol_from_large > 0 and (T - vol_from_large) % S != 0:
    vol_from_large -= L

if vol_from_large == 0 and T % S != 0:
    print("Impossible")
else:
    print(vol_from_large // L, (T - vol_from_large) // S)

