L = int(input())
H = int(input())
Target = int(input())

def sum_dig(n):
    tot = 0
    while n > 0:
        tot += n%10
        n //= 10
    return tot

valids = [i for i in range(L, H + 1) if sum_dig(i) == Target]
print(valids[0])
print(valids[-1])
