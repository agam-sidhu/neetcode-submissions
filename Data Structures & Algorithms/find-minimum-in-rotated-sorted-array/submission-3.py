class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = float('inf')
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[l] > nums[r]:
                if nums[mid] < nums[r]:
                    minNum = min(minNum, nums[mid])
                    r = mid -1
                else:
                    minNum = min(minNum, nums[mid])
                    l = mid + 1
            else:
                r = mid -1
                minNum = min(minNum, nums[mid])
        return minNum
                
                