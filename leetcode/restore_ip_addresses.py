class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return ['.'.join(ip) for ip in self.chunks(s, 4)]
    
    def chunks(self, s, ch, start=0):
        if ch == 0:
            if start == len(s):
                yield []
            return
        for end in xrange(start + 1, 1 + min(start + 3, len(s))):
            c = s[start:end]
            if (c[0] != '0' or len(c) == 1) and int(c) < 256:
                for other_chunks in self.chunks(s, ch - 1, end):
                    yield [c] + other_chunks
        
