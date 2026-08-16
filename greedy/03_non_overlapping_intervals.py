class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # print(f"Sorted {intervals}")
        removed = 0
        p1 = intervals[0]

        for i in range(1, len(intervals)):
            p2 = intervals[i]
            if p2[0] < p1[1]:
                removed += 1
            else:
                p1 = p2
        return removed
