
def pair_point(ab):
  if ab == 'xx':
    return 0
  a, b = ab
  pt = 'ABxCxD'.index
  if a == 'x':
    return pt(b)
  elif b == 'x':
    return pt(a)
  return 2 + pt(a) + pt(b)

s = input()
t = 0
for i in range(0, len(s), 2):
  t += pair_point(s[i:i+2])
print(t)

