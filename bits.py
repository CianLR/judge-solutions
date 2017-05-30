T = int(input())
for _ in range(T):
    n = input()
    most_bits = 0
    for i in range(1, len(n) + 1):
        most_bits = max(most_bits, bin(int(n[:i])).count('1'))
    print(most_bits)

