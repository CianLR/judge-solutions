class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = list(dominoes)
        last_move = None
        for i, m in enumerate(dominoes):
            if m == '.':
                continue
            elif m == 'R':
                if last_move is not None and dominoes[last_move] == 'R':
                    for j in xrange(last_move, i):
                        dominoes[j] = 'R'
            elif m == 'L':
                if last_move is None or dominoes[last_move] == 'L':
                    for j in xrange(last_move if last_move else 0, i):
                        dominoes[j] = 'L'
                elif dominoes[last_move] == 'R':
                    j, k = last_move, i
                    while k - j >= 1:
                        print j, k
                        dominoes[j] = 'R'
                        dominoes[k] = 'L'
                        j += 1
                        k -= 1
            last_move = i
        if last_move is not None and dominoes[last_move] == 'R':
            for i in xrange(last_move, len(dominoes)):
                dominoes[i] = 'R'
        return ''.join(dominoes)
                    
        
