class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        match_ind = {}
        for i, n in enumerate(nums):
            if target - n in match_ind:
                return [match_ind[target - n], i]
            match_ind[n] = i
        
