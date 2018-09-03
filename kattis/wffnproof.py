import sys

def classify(symbs):
    vs = []
    ns = []
    cs = []
    for x in symbs:
        if x in {'p', 'q', 'r', 's', 't'}:
            vs.append(x)
        elif x == 'N':
            ns.append(x)
        else:
            cs.append(x)
    return vs, ns, cs

def gen_seq(vs, ns, cs):
    if not vs:
        return 'no WFF possible'
    seq = vs.pop()
    seq = ''.join(ns) + seq
    while vs and cs:
        seq = cs.pop() + vs.pop() + seq
    return seq


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        if line == '0':
            return
        vs, ns, cs = classify(line)
        print gen_seq(vs, ns, cs)    

if __name__ == '__main__':
    main()

