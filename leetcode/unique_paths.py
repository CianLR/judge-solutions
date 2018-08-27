from math import factorial

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        n, k = m + n - 2, n - 1
        return factorial(n) / factorial(k) / factorial(n - k)
        
