class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for x in nums:
            k ^= x
        return k
        
