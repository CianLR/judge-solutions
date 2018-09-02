
def min_print_cost(K, a, b):
    for i in xrange(K):
        for j in xrange(i, K):
            if a[j] != b[j - i]:
                break
        else:
            return i
    return K

def min_scroll(K, W, words):
    if W == 0:
        return 0
    final_len = K
    for i in xrange(W - 1):
        final_len += min_print_cost(K, words[i], words[i + 1])
    return final_len

def main():
    T = int(raw_input())
    for _ in xrange(T):
        K, W = [int(x) for x in raw_input().split()]
        words = [raw_input() for _ in xrange(W)]
        print min_scroll(K, W, words)

if __name__ == '__main__':
    main()
