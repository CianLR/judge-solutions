import sys

lines = sys.stdin.readlines()
l = 0
while l < len(lines):
    _, *domain = lines[l].split()
    _, *codmain = lines[l+1].split()

    used_dom = set()
    used_codom = set()
    function = True
    injective = True
    N = int(lines[l+2])
    for i in range(N):
        d, _, c = lines[l+i+3].split()
        if d in used_dom:
            function = False
            break
        used_dom.add(d)
        if c in used_codom:
            injective = False
        used_codom.add(c)

    surjective = len(used_codom) == len(codmain)

    if not function:
        print('not a function')
    elif injective and surjective:
        print('bijective')
    elif injective:
        print('injective')
    elif surjective:
        print('surjective')
    else:
        print('neither injective nor surjective')

    l += N + 3

