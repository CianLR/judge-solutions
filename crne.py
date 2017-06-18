N = int(input())

n = (N // 2) + 1
sum_to_n = (n * (n + 1)) // 2
print(sum_to_n * 2 - (0 if N % 2 else n))
