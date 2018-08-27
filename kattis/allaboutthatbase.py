
def check_all_1(string):
    return all(map(lambda c: c == '1', string))

def base_encode(base):
    return '__23456789abcdefghijklmnopqrstuvwxyz0'[base]

def div(a, b, ans, base):
    try:
        return int(a, base) / int(b, base) == int(ans, base)
    except:
        return False
def mul(a, b, ans, base):
    try:
        return int(a, base) * int(b, base) == int(ans, base)
    except:
        return False
def add(a, b, ans, base):
    try:
        return int(a, base) + int(b, base) == int(ans, base)
    except:
        return False
def sub(a, b, ans, base):
    try:
        return int(a, base) - int(b, base) == int(ans, base)
    except:
        return False
op_map = {'/': div, '*': mul, '+': add, '-': sub}

N = int(input())

for _ in range(N):
    first, op, second, _, ans = input().split()
    working_bases = []

    if check_all_1(first) and check_all_1(second) and check_all_1(ans):
        # Unary
        if op_map[op](str(len(first)), str(len(second)), str(len(ans)), 10):
            working_bases.append('1')

    for b in range(2, 37):
        if op_map[op](first, second, ans, b):
            working_bases.append(base_encode(b))

    print(''.join(working_bases) if working_bases else 'invalid')
