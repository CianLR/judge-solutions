class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {5: 0, 10: 0, 20: 0}
        for b in bills:
            if b == 10:
                if change[5] == 0:
                    return False
                change[5] -= 1
            elif b == 20:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
            change[b] += 1
        return True
        
