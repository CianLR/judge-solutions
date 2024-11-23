import sys

def main():
  nails = [int(x) for x in sys.stdin.readlines()]
  sn = sorted(nails)
  med1 = sn[len(nails)//2]
  med2 = sn[(len(nails)//2)+1]
  mn = min(
    sum(abs(x - med1) for x in nails),
    sum(abs(x - med2) for x in nails),
  )
  print(mn)


main()