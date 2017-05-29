N = int(input())
rolls = [int(x) for x in input().split()]

for i in range(6, 0, -1):
    if rolls.count(i) == 1:
        print(rolls.index(i) + 1)
        break
else:
    print("none")

