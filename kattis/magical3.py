from itertools import combinations


class Factoriser:
    def __init__(self, limit=10000):
        self.primes = [p for p in self._primes_sieve(limit)]

    def _primes_sieve(self, limit):
        a = [True] * limit
        a[0] = a[1] = False
        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i*i, limit, 2*i):     
                    a[n] = False

    def _prime_fac(self, n):
        p = []
        i = 0
        while n != 1:
            if n % self.primes[i] == 0:
                p.append(self.primes[i])
                n //= self.primes[i]
            else:
                i += 1
        return p

    def get_factors(self, n):
        facs = set([n])
        p_f = self._prime_fac(n)
        for i in range(1, len(p_f)):
            for cmb in combinations(p_f, i):
                fac = 1
                for f in cmb:
                    fac *= f
                facs.add(fac)
        return sorted(facs)


