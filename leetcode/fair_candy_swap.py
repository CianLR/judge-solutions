class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A) - sum(B)) / 2
        b_potential = {x - diff for x in A}
        for x in B:
            if x in b_potential:
                return [x + diff, x]
        
