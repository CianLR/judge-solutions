# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda inter: (inter.start, inter.end))
        new_intervals = [intervals[0]]
        for i in xrange(1, len(intervals)):
            if new_intervals[-1].end < intervals[i].start:
                new_intervals.append(intervals[i])
            else:
                new_intervals[-1].end = max(intervals[i].end, new_intervals[-1].end)
        return new_intervals
        
        
