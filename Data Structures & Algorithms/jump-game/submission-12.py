class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # Track the farthest index we can currently reach

        for i in range(len(nums)):  # Visit each index
            if i > farthest:  # If this index is unreachable
                return False  # We cannot get to the end

            farthest = max(farthest, i + nums[i])  # Expand our reachable range

        return True  # Every index needed was reachable
        