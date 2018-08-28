INF = float("inf")

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        cur_row = triangle[0]
        for row in triangle[1:]:
            new_row = []
            for i, elm in enumerate(row):
                new_row.append(elm + min(
                    (cur_row[i - 1] if i > 0 else INF),
                    (cur_row[i] if i < len(cur_row) else INF)
                ))
            cur_row = new_row
        return min(cur_row)
