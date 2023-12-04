import sys

DIGITS = {
  '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
  '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
  'zero': 0,
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
}

def extract_int(l, start, end, it):
  for i in range(start, end, it):
    for d in DIGITS:
      if l[i:].startswith(d):
        return DIGITS[d]
  return None

def main():
  lines = sys.stdin.readlines()
  ans = 0
  for l in lines:
    left = extract_int(l, 0, len(l), 1)
    right = extract_int(l, len(l) - 1, -1, -1)
    ans += (left * 10) + right
  print(ans)

if __name__ == '__main__':
  main()