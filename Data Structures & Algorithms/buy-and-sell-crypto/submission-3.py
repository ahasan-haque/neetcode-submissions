class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy=0
        sell= 1

        while buy < sell:
            if sell >= len(prices):
                break

            prof = prices[sell] - prices[buy]
            profit = max(prof, profit)

            if prof < 0:
                buy = sell
            
            sell += 1

        return profit





