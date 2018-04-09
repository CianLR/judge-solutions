
def count_carrys(a, b):
    log = 10
    c = 0
    while log <= a * 10 or log <= b * 10:
        if (a % log) + (b % log) >= log:
            c += 1
        log *= 10
    return c

def main():
    a, b = [int(x) for x in raw_input().split()]
    while a or b:
        c = count_carrys(a, b)
        if c == 0:
            print "No carry operation."
        elif c == 1:
            print "1 carry operation."
        else:
            print c, "carry operations."
        a, b = [int(x) for x in raw_input().split()]

if __name__ == '__main__':
    main()

