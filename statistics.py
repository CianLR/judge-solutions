import sys

case_n = 1
for line in sys.stdin.readlines():
    C, *n = map(int, line.split())
    print("Case {}: {} {} {}".format(
        case_n,
        min(n),
        max(n),
        max(n) - min(n)))
    case_n += 1
