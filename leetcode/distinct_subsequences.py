class Solution:
    def numDistinct(self, s, t):
        if not s or not t:
            return int(not t)
        dp = [[0] * (len(s) + 1) for _ in xrange(len(t) + 1)]
        dp[0][:] = [1] * (len(s) + 1)
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(t) + 1):
                dp[j][i] = dp[j][i - 1]
                if s[i - 1] == t[j - 1]:
                    dp[j][i] += dp[j - 1][i - 1]
        return dp[-1][-1]

