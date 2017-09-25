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
        
        rlist = []
        # Check intervals
        for i in range(len(intervals)):
            # If the start of the current interval is less then the end of the last one change then merge
            if rlist and (rlist[-1].end >= intervals[i].start):
                rlist[-1].end = intervals[i].end
            else:
                 rlist.append(intervals[i])
            
        return rlist