N = int(input())
while N:
    first = [int(input()) for _ in range(N)]
    second = [int(input()) for _ in range(N)]
    second_to_first_pairs = {s: f for s, f in zip(sorted(second), sorted(first))}

    redone_second = [None]*N
    for s in second:
        f_equiv = second_to_first_pairs[s]
        f_ind = first.index(f_equiv)
        redone_second[f_ind] = s

    for s in redone_second:
        print(s)


    N = int(input())
    if N:
        print()
