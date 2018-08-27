class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        poss_flowers = 0
        for i in xrange(len(flowerbed)):
            if flowerbed[i]:
                continue
            if i > 0 and flowerbed[i - 1]:
                continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1]:
                continue
            flowerbed[i] = 1
            poss_flowers += 1
        return poss_flowers >= n
        
