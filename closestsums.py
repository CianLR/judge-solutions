from sys import stdin

def get_closest(nums, q):
    clo = 1000000000
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if abs(q - s) < abs(q - clo):
            clo = s
        if s > q:
            hi -= 1
        else:
            lo += 1
    return clo

def main():
    case = 1
    N = stdin.readline()
    while N.strip():
        N = int(N)
        nums = sorted([int(stdin.readline()) for _ in range(N)])
        M = int(stdin.readline())
        queries = [int(stdin.readline()) for _ in range(M)]
        print("Case {}:".format(case))
        for q in queries:
            print("Closest sum to {} is {}.".format(q, get_closest(nums, q)))
        case += 1
        N = stdin.readline()

if __name__ == '__main__':
    main()

