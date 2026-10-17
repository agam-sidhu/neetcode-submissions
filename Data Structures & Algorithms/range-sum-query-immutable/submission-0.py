class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]*len(nums)
        i = 0
        total = 0
        while i < len(nums):
            self.prefix[i] = total + nums[i]
            total += nums[i]
            i+=1
            

        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]

        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)