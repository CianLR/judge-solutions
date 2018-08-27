class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        if neg:
            x *= -1
        x = int(str(x)[::-1])
        x *= -1 if neg else 1
        return x if -2**31 <= x <= 2**31 - 1 else 0
        
