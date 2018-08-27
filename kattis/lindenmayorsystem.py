
def apply_rules(s, rules):
    return ''.join(map(lambda c: rules.setdefault(c, c), s))

def evaluate(s, rules, iterations):
    for _ in range(iterations):
        s = apply_rules(s, rules)
    return s

def main():
    N, M = map(int, input().split())
    rules = {}
    for _ in range(N):
        f, _, t = input().split()
        rules[f] = t
    seed = input()
    print(evaluate(seed, rules, M))


if __name__ == '__main__':
    main()

