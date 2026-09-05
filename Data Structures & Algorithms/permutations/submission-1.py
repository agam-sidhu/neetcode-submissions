class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        curr = []
        res = []
        def dfs():
            if len(curr) == len(nums):  # If every number has been chosen
                res.append(curr.copy())  # Save this permutation
                return  # Stop this branch
            for num in nums:  # Try every number as the next choice
                if num in used:  # Skip numbers already chosen
                    continue  
                curr.append(num)  # Choose the number
                used.add(num)  # Mark it as used
                dfs()  # Explore further
                curr.pop()
                used.remove(num)
        dfs()
        return res