from itertools import izip_longest

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        out = ''
        carry = 0
        for a, b in izip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            carry, s = divmod((ord(a) - ord('0')) +
                              (ord(b) - ord('0')) +
                              carry,
                              10)
            out += str(s)
        if carry:
            out += str(carry)
        return out[::-1]
        
