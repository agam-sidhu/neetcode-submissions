class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        intervals.sort
        for next_interval in intervals[1:]:
            if next_interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], next_interval[1])
            else:
                res.append(next_interval)
        return res