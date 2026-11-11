class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        j = len(prices)-1
        maxProfit = 0
        while j>=0:
            if prices[j]>=s:
                s = prices[j]
            else:
                profit = s-prices[j]
                maxProfit = max(profit, maxProfit)

            j-=1
        return maxProfit

        