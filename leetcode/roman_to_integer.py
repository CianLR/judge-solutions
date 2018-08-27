class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        replaces = {
            'IV': 'I' * 4,
            'IX': 'I' * 9,
            'XL': 'X' * 4,
            'XC': 'X' * 9,
            'CD': 'C' * 4,
            'CM': 'C' * 9
        }
        vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for rep in replaces:
            s = s.replace(rep, replaces[rep])
        n = 0
        for c in s:
            n += vals[c]
        return n
        
