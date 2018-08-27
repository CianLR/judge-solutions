class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        look = place = 0
        while look < len(nums):
            if nums[look] != val:
                nums[place] = nums[look]
                place += 1
            look += 1
        return place

