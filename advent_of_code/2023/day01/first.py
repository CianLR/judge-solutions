import sys


def extract_int(l):
  i = ''
  for c in l:
    if c.isdigit():
      i += c
      break
  for c in reversed(l):
    if c.isdigit():
      i += c
      break
  return int(i)

def main():
  lines = sys.stdin.readlines()
  ans = 0
  for l in lines:
    ans += extract_int(l)
  print(ans)

if __name__ == '__main__':
  main()