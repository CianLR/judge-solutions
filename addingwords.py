import sys

VARS = {}
INTS = {}

def calc(*args):
    var = args[::2]
    ops = ('+',) + args[1::2]
    res = 0
    for i in range(len(var)):
        if var[i] not in VARS:
            return ' '.join(args) + ' unknown'
        res += VARS[var[i]] * (1 if ops[i] == '+' else -1)
    return ' '.join(args + (INTS[res] if res in INTS else 'unknown',))

def clear():
    VARS.clear()
    INTS.clear()

def define(v, i):
    if v in VARS:
        del INTS[VARS[v]]
    VARS[v] = int(i)
    INTS[int(i)] = v

CMDS = {
    'calc': calc,
    'clear': clear,
    'def': define
}

def main():
    for line in sys.stdin.readlines():
        if not line.strip():
            continue
        cmd, *args = line.split()
        out = CMDS[cmd](*args)
        if out:
            print(out)

if __name__ == '__main__':
    main()

