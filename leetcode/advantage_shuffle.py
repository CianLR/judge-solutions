class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        b_sort = sorted((e, i) for i, e in enumerate(B))
        a_sort = sorted(A)
        a_new = [None] * len(A)
        as_i = 0
        unused = []
        for eb, i in b_sort:
            while as_i < len(a_sort) and a_sort[as_i] <= eb:
                unused.append(a_sort[as_i])
                as_i += 1
            if as_i == len(a_sort):
                break
            a_new[i] = a_sort[as_i]
            as_i += 1
        
        unused_i = 0
        for i in range(len(a_new)):
            if a_new[i] is None:
                a_new[i] = unused[unused_i]
                unused_i += 1
        return a_new
        
