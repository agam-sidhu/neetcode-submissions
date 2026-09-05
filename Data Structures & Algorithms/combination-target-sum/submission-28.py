class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        

        def dfs(i, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return 
            if remaining <0:
                return
            if i == len(nums):
                return
            curr.append(nums[i])
            dfs(i, remaining - nums[i])
            curr.pop()
            dfs(i+1, remaining)
        dfs(0, target)
        return res
        