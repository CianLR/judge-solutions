from sys import stdin

def define(definitions, args):
    i, v = args.split()
    definitions[v] = int(i)

def compare(definitions, args):
    a, c, b = args.split()
    if a not in definitions or b not in definitions:
        return 'undefined'
    ai, bi = definitions[a], definitions[b]
    res = None
    if c == '=':
        res = ai == bi
    elif c == '<':
        res = ai < bi
    else:
        res = ai > bi
    return 'true' if res else 'false'

CMDS = {'define': define, 'eval': compare}

def main():
    definitions = {}
    for line in stdin.readlines():
        cmd, args = line.strip().split(' ', 1)
        out = CMDS[cmd](definitions, args)
        if out:
            print(out)

if __name__ == '__main__':
    main()

