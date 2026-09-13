class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x :x[0])
        total = 0
        prev_end = intervals[0][1]
        for current in intervals[1:]:
            if prev_end > current[0]:
                prev_end = min(prev_end, current[1])
                total+=1
            else:
                prev_end = current[1]

        return total

        