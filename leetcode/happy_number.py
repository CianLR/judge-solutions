def nextnum(n):
    return sum(x**2 for x in map(int, str(n)))

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {n}
        while n != 1:
            n = nextnum(n)
            if n in seen:
                return False
            seen.add(n)
        return True
        
