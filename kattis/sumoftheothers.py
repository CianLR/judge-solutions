import sys

for line in sys.stdin.readlines():
    nums = list(map(int, line.split()))
    print(sum(nums) // 2)
