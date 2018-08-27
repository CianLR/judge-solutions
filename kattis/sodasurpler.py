e, f, c = map(int, input().split())

total_drank = 0
total_empties = e + f
while total_empties >= c:
    total_drank += total_empties // c
    total_empties = (total_empties // c) + (total_empties % c)

print(total_drank)
