class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a_dict = {e: i for i, e in enumerate(A)}
        seen = {}
        max_chain = 0
        for i in xrange(len(A) - 2):
            for j in xrange(i + 1, len(A) - 1):
                if (i, j) in seen:
                    continue
                a, b = i, j
                path = [(a, b)]
                chain_len = 0
                while A[a] + A[b] in a_dict:
                    a, b = b, a_dict[A[a] + A[b]]
                    chain_len += 1
                    if (a, b) in seen:
                        chain_len += seen[(a, b)]
                        break
                    path.append((a, b))
                    
                if chain_len:
                    chain_len += 2
                if chain_len > max_chain:
                    max_chain = chain_len
                for p in path:
                    seen[p] = chain_len
                    chain_len -= 1
        return max_chain
                
                    
        
