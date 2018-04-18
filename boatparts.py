
def main():
    P, N = (int(x) for x in raw_input().split())
    replaced = set()
    last_new_replace = -1
    for day in range(1, N + 1):
        part = raw_input()
        if part not in replaced:
            replaced.add(part)
            last_new_replace = day
    if len(replaced) == P:
        print last_new_replace
    else:
        print "paradox avoided"


if __name__ == '__main__':
    main()

