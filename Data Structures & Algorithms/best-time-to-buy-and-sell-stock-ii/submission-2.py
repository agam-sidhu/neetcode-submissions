class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0                                      # Total profit from all profitable transactions

        for i in range(1, len(prices)):                 # Start from second day
            if prices[i] > prices[i - 1]:               # If price increased from yesterday
                profit += prices[i] - prices[i - 1]     # Capture that positive gain

        return profit                                   # Return total accumulated profit