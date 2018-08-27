from random import randrange

class Solution(object):
    def primePalindrome(self, N):
        a = self.first_check(N)
        if a is not None:
            return a
        count = self.start(N)
        print count
        while True:
            k = int(str(count)[:-1] + str(count)[::-1])
            if k >= N and self.is_prime(k):
                print count
                return k
            count += 1
            

    def start(self, N):
        sn = str(N)
        if len(sn) % 2 == 0:
            return 10 ** (len(sn) / 2)
        a = int(sn[:1+len(sn)/2])
        b = int(sn[len(sn)/2:][::-1])
        print a, b
        if a > b:
            return b
        return a

    def first_check(self, N):
        lst = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471, 17971, 18181]
        for l in lst:
            if l >= N:
                return l
        return None

    def is_prime(self, k, iters=10):
        if k < 2:
            return False
        if not k & 1:
            return k == 2
        smallprimes = (3,5,7,11,13,17,19,23,29,31,37,41,43,
                       47,53,59,61,67,71,73,79,83,89,97)
        for sp in smallprimes:
            if k % sp == 0:
                return k == sp

        s, d = 0, k - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        for _ in xrange(iters):
            a = randrange(2, k - 1)
            if not self.check_witness(a, s, d, k):
                return False
        return True

    def check_witness(self, a, s, d, n):
        q = pow(a, d, n)
        if q == 1:
            return True
        for _ in xrange(s - 1):
            if q == n - 1:
                return True
            q = pow(q, 2, n)
        return q == n - 1

if __name__ == '__main__':
    pass
    #s = Solution()
    #s.primePalindrome(1215122)
