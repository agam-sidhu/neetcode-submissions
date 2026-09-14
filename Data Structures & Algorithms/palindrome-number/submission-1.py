class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)              # Convert integer to string
        return s == s[::-1]     # Compare with reversed string
        