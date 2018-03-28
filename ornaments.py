from math import pi, acos

def strand_length(r, h):
    return 2 * (h ** 2 - r ** 2) ** 0.5

def circle_ratio(r, h):
    return 1 - (acos(r / h) / pi)

def string_length(r, h, s):
    strand = strand_length(r, h)
    circle_len = circle_ratio(r, h) * 2 * pi * r
    return (circle_len + strand) * (1 + s/100)

def main():
    r, h, s = [int(x) for x in input().split()]
    while r or h or s:
        print("{:.2f}".format(string_length(r, h, s)))
        r, h, s = [int(x) for x in input().split()]

if __name__ == '__main__':
    main()

