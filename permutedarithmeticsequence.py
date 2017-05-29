
def is_arith(seq):
    stride = seq[1] - seq[0]
    for a, b in zip(seq, seq[1:]):
        if b - a != stride:
            return False
    return True

N = int(input())
for _ in range(N):
    K, *ks = map(int, input().split())
    if is_arith(ks):
        print("arithmetic")
    elif is_arith(sorted(ks)):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")
