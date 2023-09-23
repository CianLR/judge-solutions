class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = []
        i = 0
        for n in nums2:
          while i < len(nums1):
            if n <= nums1[i]:
              nums1.insert(i, n)
              print(i, "at", n)
              break
            else:
              i += 1
              print(i)
          if i == len(nums1):
            nums1.insert(i, n)
        
