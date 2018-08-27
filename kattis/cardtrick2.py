
def rot_list_right(l, num):
    num %= len(l)
    ret = [0] * len(l)
    for i, j in enumerate(range(-num, len(l) - num)):
        ret[i] = l[j]
    return ret

def main():
    N = int(input())
    for _ in range(N):
        K = int(input())
        cards = []
        for k in range(K, 0, -1):
            cards = rot_list_right([k] + cards, k)
        print(*cards)

if __name__ == '__main__':
    main()

