

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
    return l

def main():
    poly = raw_input()
    l = react(list(poly))
    print len(l)

if __name__ == '__main__':
    main()
