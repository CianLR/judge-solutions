class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1        
        for i in xrange(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
            if not carry:
                break
        return ([1] + digits) if carry else digits
        
