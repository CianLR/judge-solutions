
def largest_sum(lst):
    lstart = start = end = largest = s = 0
    for i, v in enumerate(lst):
        s += v
        if s < 0:
            s = 0
            start = i + 1
        if s > largest:
            largest = s
            end = i
            lstart = start
    return lstart, end, largest

def main():
    rains = raw_input()
    rs, re, rl = largest_sum(1 if c == 'R' else -1 for c in rains)
    bs, be, bl = largest_sum(1 if c == 'B' else -1 for c in rains)
    _, s, e = min((-rl, rs, re), (-bl, bs, be))
    print s + 1, e + 1

if __name__ == '__main__':
    main()

