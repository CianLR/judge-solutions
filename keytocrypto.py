
vals = {chr(c): c - ord('A') for c in range(ord('A'), ord('Z') + 1)}
chrs = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

def shift(c, n):
    v = vals[c]
    n = n if type(n) == int else vals[n]
    return chrs[(v + n) % len(chrs)]

def main():
    cyp = input()
    key = input()

    if len(key) >= len(cyp):
        print(''.join(shift(cyp[i], -vals[key[i]]) for i in range(len(cyp))))
        return

    orig = [shift(cyp[i], -vals[key[i]]) for i in range(len(key))]
    for i in range(len(key), len(cyp)):
        oc = orig[i - len(key)]
        orig.append(shift(cyp[i], -vals[oc]))
    
    print(''.join(orig))

if __name__ == '__main__':
    main()

