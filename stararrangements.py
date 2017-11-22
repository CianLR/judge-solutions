
def get_divs(N):
    d = []
    for i in range(1, int(N**0.5 + 1)):
        if N % i == 0:
            d.append(i)
            d.append(N // i)
    return sorted(d)

#def main():
#    N = int(input())
#    divs = get_divs(N)
#    combs = set()
#    for d in divs:
#        if d % 2 == 0:
#            combs.add((d, d))
#        a, b = (d // 2) + 1, d // 2
#        if b == 0:
#            continue
#        if (N - a) % (a + b) == 0:
#            combs.add((a, b))
#        elif N % (a + b) == 0:
#            combs.add((a, b))
#
#        a, b = d // 2, (d // 2) - 1
#        if b == 0:
#            continue
#        if (N - a) % (a + b) == 0:
#            combs.add((a, b))
#        elif N % (a + b) == 0:
#            combs.add((a, b))
#
#    for a, b in sorted(combs):
#        print("{},{}".format(a, b))

def check_valid(N, a, b):
    return N % (a + b) == 0 or (N - a) % (a + b) == 0

def main():
    N = int(input())
    print("{}:".format(N))
    combs = set()
    for a in range(1, (N // 2) + 1):
        if check_valid(N, a, a) and a != 1:
            combs.add((a, a))
        if check_valid(N, a + 1, a):
            combs.add((a + 1, a))
    for a, b in sorted(combs):
        print("{},{}".format(a, b))

if __name__ == '__main__':
    main()

