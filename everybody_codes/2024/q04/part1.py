import sys

def main():
  nails = [int(x) for x in sys.stdin.readlines()]
  mn = min(nails)
  print(sum(x - mn for x in nails))

main()