from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(x) for x in range(1, n + 1)]
        return self.get_perm(nums, k - 1)
    
    def get_perm(self, nums, k):
        n = len(nums)
        if n == 1:
            return nums[0]
        segment_size = factorial(n - 1)
        seg_i = k / segment_size
        front = nums[seg_i]
        nums = nums[:seg_i] + nums[seg_i + 1:]
        return front + self.get_perm(nums, k % segment_size)
        
