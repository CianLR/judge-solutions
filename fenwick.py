from sys import stdin

class FenwickTree:
    def __init__(self, N):
        self.table = [0] * (N + 1)

    def get_sum(self, i):
        range_sum = 0
        while i:
            range_sum += self.table[i]
            i -= i & -i
        return range_sum
    
    def set_index(self, i, delta):
        while i < len(self.table):
            self.table[i] += delta
            i += i & -i

def main():
    N, Q = [int(x) for x in stdin.readline().split()]
    ft = FenwickTree(N)
    for _ in xrange(Q):
        args = stdin.readline().split()
        if args[0] == '+':
            ind, val = args[1:]
            ft.set_index(int(ind) + 1, int(val))
        else:
            print ft.get_sum(int(args[1]))

if __name__ == '__main__':
    main()
    
