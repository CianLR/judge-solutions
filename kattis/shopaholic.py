print(0) if int(input()) < 3 else print(sum(sorted(map(int, input().split()))[-3::-3]))
