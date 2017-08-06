
def get_diff(l):
    if len(l) == 0:
        return 0, -1
    if not any(l):
        return l[0], -1
    difs = []
    for a, b in zip(l, l[1:]):
        difs.append(b - a)
    
    n_diff, i = get_diff(difs)
    return l[-1] + n_diff, i + 1

def main():
    N, *l = [int(x) for x in input().split()]
    next_val, i = get_diff(l)
    print(i, next_val)

if __name__ == '__main__':
    main()

