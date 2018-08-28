class Solution:
    def isInterleave(self, s1, s2, s3):
        self.memo = [
                [
                    [None] * len(s3) + 1 for _ in xrange(len(s2) + 1)
                ] for _ in xrange(len(s1) + 1)
        ]
        return self.match(s1, s2, s3, 0, 0, 0)

    def match(self, s1, s2, s3, i, j, k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        if self.memo[i][j][k] is not None:
            return self.memo[i][j][k]
        if (    i < len(s1) and k < len(s3) and
                s1[i] == s3[k] and
                self.match(s1, s2, s3, i + 1, j, k + 1)):
            self.memo[i][j][k] = True
        elif (    j < len(s2) and k < len(s3) and
                s2[j] == s3[k] and
                self.match(s1, s2, s3, i, j + 1, k + 1)):
            self.memo[i][j][k] = True
        else:
            self.memo[i][j][k] = False
        return self.memo[i][j][k]
