
def tri_point(ab):
  counts = 0
  pts = 0
  for c in ab:
    if c != 'x':
      counts += 1
      pts += 'ABxCxD'.index(c)
  # print(pts, counts)
  bonus = 0
  if counts == 2:
    bonus = 2
  elif counts == 3:
    bonus = 6
  return pts + bonus

s = input()
t = 0
for i in range(0, len(s), 3):
  t += tri_point(s[i:i+3])
  # print(t)
print(t)

