class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # Define the function.
        res = [1] * len(nums)  # Create the output array, initialized with 1s.
        prefix = 1  # Store the running product of everything to the left.
        for i in range(len(nums)):  # Move from left to right.
            res[i] = prefix  # Store the product of everything before index i.
            prefix *= nums[i]  # Include the current number for the next position.
        postfix = 1  # Store the running product of everything to the right.
        for i in range(len(nums) - 1, -1, -1):  # Move from right to left.
            res[i] *= postfix  # Multiply the left product by the right product.
            postfix *= nums[i]  # Include the current number for the next position to the left.
        return res  # Return the completed answer.
        