class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        place = look = 0
        while look < len(nums):
            if nums[look] != nums[place]:
                place += 1
                nums[place] = nums[look]
            look += 1
        return place + 1
        
