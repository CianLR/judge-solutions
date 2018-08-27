from itertools import permutations

pow_combs = set()

for i in xrange(30):
    pow_combs.add(tuple(sorted(str(1 << i))))

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return tuple(sorted(str(N))) in pow_combs
        
