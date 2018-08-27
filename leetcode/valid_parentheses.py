from collections import deque

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        open_to_close = {'{': '}', '[': ']', '(': ')'}
        for b in s:
            if b in open_to_close:
                stack.append(open_to_close[b])
            elif not stack or stack.pop() != b:
                return False
        return not bool(stack)
        
