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
        if not intervals:
            return intervals
        inters = []
        for each in intervals:
            inters.append([each.start,each.end])
        inters.sort(key = lambda x:x[0])
        res = [inters[0]]
        for each in inters[1:]:
            if each[0] <= res[-1][1]:
                if each[1] >= res[-1][1]:
                    res[-1][1] = each[1]
            else:
                res.append(each)
        return res