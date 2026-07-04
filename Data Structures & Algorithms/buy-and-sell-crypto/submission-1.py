class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
            if prices[right] < prices[left]:
                left = right

        return maxProfit