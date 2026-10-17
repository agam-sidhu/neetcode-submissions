class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        for i in range(len(nums)):
            leftSum = prefix[i]
            rightSum = prefix[len(nums)] - prefix[i+1]
            if leftSum == rightSum:
                return i
        return -1 
        

            
         

        