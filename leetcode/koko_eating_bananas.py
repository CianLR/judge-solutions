from math import ceil

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        if H == len(piles):
            return max(piles)
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo+hi)/2
            if self.check_banana(piles, mid) > H: lo = mid+1
            else: hi = mid
        return lo
    
    def check_banana(self, piles, k):
        k = float(k)
        h = 0
        for b in piles:
            h += int(ceil(b / k))
        return h
        
