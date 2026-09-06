class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one = 1
        two = 2
        for step in range(3, n+1):
            current = one + two
            one = two
            two = current
        return two