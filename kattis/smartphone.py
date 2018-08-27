
def common_prefix(a, b):
    small_len = min(len(a), len(b))
    for i in range(small_len):
        if a[i] != b[i]:
            return i
    return small_len


def main():
    N = int(input())
    for _ in range(N):
        wanted = input()
        have = input()
        sug = [input() for _ in range(3)]

        # Keep typing
        keep_cost = 0
        pfx = common_prefix(wanted, have)
        keep_cost += len(have) - pfx
        keep_cost += len(wanted) - pfx

        # Each suggestion
        sugg_costs = [keep_cost]
        for s in sug:
            cost = 1
            pfx = common_prefix(wanted, s)
            cost += len(s) - pfx
            cost += len(wanted) - pfx
            sugg_costs.append(cost)

        print(min(sugg_costs))


if __name__ == '__main__':
    main()

