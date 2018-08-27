class Solution(object):
    def longestPalindrome(self, S):
        """
        :type s: str
        :rtype: str
        """
        if len(S) == 0:
            return ''
        dp = [[False] * len(S) for _ in xrange(len(S) + 1)]
        dp[0] = [True] * len(S)  # Palindromes of len 0
        dp[1] = [True] * len(S)  # Palindromes of len 1
        prev_has_palin = True
        has_palin = True
        l = 1
        for l in xrange(2, len(S) + 1):
            prev_has_palin, has_palin = has_palin, False
            for s in xrange(len(S) - (l - 1)):
                if dp[l - 2][s + 1] and S[s] == S[s + (l - 1)]:
                    dp[l][s] = True
                    has_palin = True
            if not prev_has_palin and not has_palin:
                break
        else:
            l += 2 if has_palin else 1  # Case where loop doesn't break
        for s in xrange(len(S)):
            if dp[l - 2][s]:
                return S[s:s + (l - 2)]
        raise Exception("what")
