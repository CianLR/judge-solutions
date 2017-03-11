init, *pref = input()

curr = init
# Always up
changes_up = 0
for p in pref:
    if curr != p:
        changes_up += 1
        curr = p
    if curr != 'U':
        changes_up += 1
        curr = 'U'
print(changes_up)

curr = init
# Always down
changes_down = 0
for p in pref:
    if curr != p:
        changes_down += 1
        curr = p
    if curr != 'D':
        changes_down += 1
        curr = 'D'
print(changes_down)

curr = init
# Always down
changes_oth = 0
for p in pref:
    if curr != p:
        changes_oth += 1
        curr = p
print(changes_oth)
