class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        lo, hi = 1, x
        while lo < hi:
            mid = (lo + hi) / 2
            if x < mid * mid:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
        
