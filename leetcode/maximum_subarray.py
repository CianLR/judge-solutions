class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_sum = max(nums)
        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum < 0:
                curr_sum = 0
            else:
                largest_sum = max(largest_sum, curr_sum)
        return largest_sum
