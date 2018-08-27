N, S, R = map(int, input().split())
dams = {int(x) for x in input().split()}
reser = {int(x) for x in input().split()}

using_own = dams & reser
dams -= using_own
reser -= using_own

for r in reser:
    if r - 1 in dams:
        dams.remove(r - 1)
    elif r + 1 in dams:
        dams.remove(r + 1)

print(len(dams))
