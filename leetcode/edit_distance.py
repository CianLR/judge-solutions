class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a = [[None] * (len(word2) + 1) for _ in xrange(len(word1) + 1)]
        for r in xrange(len(word1) + 1):
            a[r][0] = r
        for c in xrange(len(word2) + 1):
            a[0][c] = c
        for r in xrange(1, len(word1) + 1):
            for c in xrange(1, len(word2) + 1):
                a[r][c] = min(
                    a[r - 1][c - 1] + (word1[r-1] != word2[c-1]),
                    a[r - 1][c] + 1,
                    a[r][c - 1] + 1
                )
        return a[-1][-1]
        
