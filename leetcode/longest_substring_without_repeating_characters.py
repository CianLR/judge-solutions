class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        max_len = 0
        curr_len = 0
        start = 0
        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= start:
                curr_len = i - last_seen[c]
                start = last_seen[c]
            else:
                curr_len += 1
            last_seen[c] = i
            if curr_len > max_len:
                max_len = curr_len
        return max_len
        
