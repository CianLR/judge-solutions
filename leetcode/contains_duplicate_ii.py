class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_ind = {}
        for i in xrange(len(nums)):
            if nums[i] in last_ind and i - last_ind[nums[i]] <= k:
                return True
            last_ind[nums[i]] = i
        return False
        
