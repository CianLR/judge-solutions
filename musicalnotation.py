
def get_default():
    return [' ', '-', ' ', '-', ' ', '-', ' ', '-', ' ', '-', ' ', ' ', ' ', '-']


N = int(input())
notes = input().split()

note_idx = 'GFEDCBAgfedcba'

cols = []
cols.append(list(note_idx))
cols.append([':']*14)
cols.append([' ']*14)

for nt in notes:
    mult = 1
    if len(nt) == 2:
        mult = int(nt[1])
        nt = nt[0]
    filled = get_default()
    filled[note_idx.index(nt)] = '*'
    for _ in range(mult):
        cols.append(filled)
    cols.append(get_default())

cols = cols[:-1]  # Chop off last spacer
for line in zip(*cols):
    print(''.join(line))
