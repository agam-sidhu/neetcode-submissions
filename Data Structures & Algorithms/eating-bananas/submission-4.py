class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            k = (left + right) // 2
            time = 0
            for p in piles:
                time += (p + k - 1) // k
            if time > h:
                left = k + 1
            else:
                right = k
            
        return left