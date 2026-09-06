class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentTotal = nums[0]
        maxTotal = nums[0]

        for n in nums[1:]:
            currentTotal = max(n, currentTotal + n)
            maxTotal = max(maxTotal, currentTotal)
        return maxTotal
        