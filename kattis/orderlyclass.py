
def rev_eq(a, b, s, e):
  reva = a[:s] + a[s:e+1][::-1] + a[e+1:]
  return reva == b

def main():
  start = raw_input()
  end =   raw_input()
  s, e = 0, len(start) - 1
  while start[s] == end[s]:
    s += 1
  while start[e] == end[e]:
    e -= 1
  count = 0
  while s >= 0 and e < len(end) and rev_eq(start, end, s, e):
    s -= 1
    e += 1
    count += 1
  print count

if __name__ == '__main__':
  main()

