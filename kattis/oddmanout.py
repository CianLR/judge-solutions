T = int(input())
for t in range(1, T + 1):
    G = int(input())
    guest_nums = list(map(int, input().split()))
    print(
        "Case #{}:".format(t),
        min(guest_nums, key=lambda g: guest_nums.count(g)))