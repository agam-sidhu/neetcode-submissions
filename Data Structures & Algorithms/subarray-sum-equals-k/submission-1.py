class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        result = 0

        for n in nums:
            current_sum += n
            diff = current_sum - k
            result+= prefix_count.get(diff, 0)
            prefix_count[current_sum] = 1 + prefix_count.get(current_sum, 0)

        return result
        