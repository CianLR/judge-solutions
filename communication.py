N = int(input())
ans = []
for b in map(int, input().split()):
    orig = [0]
    binary_repr = bin(b)[2:]
    binary_repr = '0'*(8 - len(binary_repr)) + binary_repr
    for c in binary_repr[::-1]:
        orig.append(str(int(c) ^ int(orig[-1])))
    ans.append(int(''.join(orig[1:][::-1]), 2))
print(*ans)    
