class Solution:
     def threeSum(self, nums: List[int]) -> List[List[int]]:  # Define the 3Sum function.
        nums.sort()  # Sort the array so two pointers can be used.
        result = []  # Store all unique triplets.
        for i in range(len(nums)):  # Treat each index as the fixed first number.
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate fixed numbers.
                continue  # Move to the next possible fixed number.
            left = i + 1  # Start the left pointer just after the fixed number.
            right = len(nums) - 1  # Start the right pointer at the end.
            while left < right:  # Continue while the two pointers have not crossed.
                total = nums[i] + nums[left] + nums[right]  # Compute the three-number sum.
                if total == 0:  # Check whether we found a valid triplet.
                    result.append([nums[i], nums[left], nums[right]])  # Save the triplet.
                    left += 1  # Move the left pointer inward.
                    right -= 1  # Move the right pointer inward.
                    while left < right and nums[left] == nums[left - 1]:  # Skip duplicate left values.
                        left += 1  # Continue moving left forward.
                    while left < right and nums[right] == nums[right + 1]:  # Skip duplicate right values.
                        right -= 1  # Continue moving right backward.
                elif total < 0:  # If the sum is too small.
                    left += 1  # Move left rightward to increase the sum.
                else:  # If the sum is too large.
                    right -= 1  # Move right leftward to decrease the sum.
        return result  # Return all unique triplets.

