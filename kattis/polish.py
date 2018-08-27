from sys import stdin

ops = {
    '+': lambda x, y: str(int(x) + int(y)),
    '-': lambda x, y: str(int(x) - int(y)),
    '*': lambda x, y: str(int(x) * int(y)),
}

def is_int(s):
    return s.isdigit() or (len(s) > 0 and s[0] == '-' and s[1:].isdigit())

def pn(expr, i=0):
    if is_int(expr[i]) or expr[i] not in ops:
        return expr[i], i + 1
    op = expr[i]
    sub1, i = pn(expr, i + 1)
    sub2, i = pn(expr, i)
    if is_int(sub1) and is_int(sub2):
        return ops[op](sub1, sub2), i
    return op + ' ' + sub1 + ' ' + sub2, i

def main():
    for i, line in enumerate(stdin.readlines()):
        print("Case {}:".format(i + 1), pn(line.strip().split())[0])


if __name__ == '__main__':
    main()

