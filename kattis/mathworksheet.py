import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

MAX_COL = 50

def calc(a, op, b):
    return str(OPS[op](int(a), int(b)))

def main():
    N = int(input())
    while N:
        ans = [calc(*input().split()) for _ in range(N)]
        longest = max(len(x) for x in ans)
        padded_ans = ['{:>{}}'.format(x, longest) for x in ans]
        cols = (MAX_COL + 1) // (longest + 1)
        for i in range(0, len(padded_ans), cols):
            print(*padded_ans[i:i + cols])
        N = int(input())
        if N:
            print()

if __name__ == '__main__':
    main()

