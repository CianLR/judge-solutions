class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones  = 0
        for i, e in enumerate(nums):
            nums[i] = 2
            if e < 2:
                nums[ones] = 1
                ones += 1
            if e < 1:
                nums[zeros] = 0
                zeros += 1
        
