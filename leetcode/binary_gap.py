class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        big_dist = 0
        one_dist = None
        for c in bin(N):
            if one_dist is None:
                if c == '1':
                    one_dist = 0
            else:
                one_dist += 1
                if c == '1':
                    big_dist = max(one_dist, big_dist)
                    one_dist = 0
        return big_dist
        
