N = input()
temps = [0 if int(i) >= 0 else 1 for i in input().split()]
print(sum(temps))