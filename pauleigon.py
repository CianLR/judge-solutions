N, P, Q = map(int, input().split())

rounds_played = P + Q
print(['paul', 'opponent'][(rounds_played//N)%2])
