import sys

for l in sys.stdin.readlines():
    month, day, year, start, end = l.split()
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))

    h = eh - sh - (sm > em)
    m = (em - sm) % 60

    print(month, day, year, h, "hours", m, "minutes")
