class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        removal = 0
        for curr in intervals[1:]:
            if curr[0] < prev_end:
                removal +=1
                prev_end = min(curr[1], prev_end)
            else:
                prev_end = curr[1]
        return removal
        