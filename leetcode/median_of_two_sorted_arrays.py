class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        even = (len(nums1) + len(nums2)) % 2 == 0
        mid = (len(nums1) + len(nums2)) // 2
        gen = self.combine(nums1, nums2)
        if even:
            for _ in range(mid - 1):
                next(gen)
            return (next(gen) + next(gen)) / 2
        else:
            for _ in range(mid):
                next(gen)
            return next(gen)
    
    def combine(self, nums1, nums2):
        f = s = 0
        while f < len(nums1) and s < len(nums2):
            if nums1[f] < nums2[s]:
                yield nums1[f]
                f += 1
            else:
                yield nums2[s]
                s += 1
        yield from nums1[f:]
        yield from nums2[s:]
        
