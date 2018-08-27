class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        spl = filter(None, s.split(' '))
        return len(spl[-1]) if spl else 0
        
