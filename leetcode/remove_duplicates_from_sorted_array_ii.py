
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        last = 1
        for i in xrange(2, len(nums)):
            if nums[i] != nums[last] or (nums[i] == nums[last] and nums[last] != nums[last - 1]):
                last += 1
                nums[last] = nums[i]
        return last + 1
        
