

def does_react(a, b):
    return a != b and a.lower() == b.lower()

def react(l):
    changes = True
    while changes:
        nl = []
        changes = False
        i = 0
        while i < len(l):
            if i < len(l) - 1 and does_react(l[i], l[i + 1]):
                i += 2
                changes = True
            else:
                nl.append(l[i])
                i += 1
        l = nl
    return len(l)

def rm_unit(l, u):
    return [c for c in l if c.lower() != u.lower()]

def find_shortest(poly):
    uniq = set(poly.lower())
    return min(react(rm_unit(list(poly), u)) for u in uniq)

def main():
    poly = raw_input()
    print find_shortest(poly)

if __name__ == '__main__':
    main()
