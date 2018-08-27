from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        return list(anagrams.values())
        
