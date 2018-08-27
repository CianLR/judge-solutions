import heapq

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = nums[0]
        i = 1
        while i <= farthest and i < len(nums):
            farthest = max(farthest, nums[i] + i)
            i += 1
        return i >= len(nums)
        
