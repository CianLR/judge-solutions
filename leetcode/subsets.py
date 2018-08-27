class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = []
        for i in xrange(len(nums) + 1):
            subs += list(self.get(nums, i))
        return subs
        
    def get(self, nums, n, start=0):
        if n == 0:
            yield []
            return
        for i in xrange(start, 1 + len(nums) - n):
            for perm in self.get(nums, n - 1, i + 1):
                yield [nums[i]] + perm
        
