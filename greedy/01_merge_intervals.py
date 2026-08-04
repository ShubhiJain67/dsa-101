class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        p1 = 0
        p2 = 1
        while p2 < len(intervals):
            # print(f"{p1} {p2} {intervals}")
            if intervals[p1][1] >= intervals[p2][0]:
                intervals = intervals[:p1] + [[min(intervals[p1][0], intervals[p2][0]), max(intervals[p1][1], intervals[p2][1])]] + intervals[p2+1:]
            else:
                p1 += 1
                p2 += 1
            
        return intervals
