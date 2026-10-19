class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        for n in nums:
            count[n] = 1 + count.get(n , 0)
        for n, cnt in count.items():
            freq.append([cnt, n])
        freq.sort()
        res = []
        while len(res) < k:
            res.append(freq.pop()[1])
        return res
            