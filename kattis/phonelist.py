T = int(input())
for _ in range(T):
    N = int(input())
    nums = sorted([input() for _ in range(N)])
    for i in range(1, len(nums)):
        if nums[i].startswith(nums[i - 1]):
            print('NO')
            break
    else:
        print('YES')

