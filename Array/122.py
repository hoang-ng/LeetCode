class Solution1:
    def maxProfit(self, prices):
        i = len(prices) - 1
        j = i - 1
        
        maxProfit = 0
        totalProfit = 0
        while (i >= 0 and j >= 0):
            if (prices[i] < prices[j]):
                i = j
            elif maxProfit < prices[i] - prices[j]:
                maxProfit = prices[i] - prices[j]
            else:
                totalProfit += maxProfit
                maxProfit = 0
                i = j
            j = i - 1
        return totalProfit

class Solution2:
    def maxProfit(self, prices):
        totalProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                totalProfit += prices[i] - prices[i - 1]
        return totalProfit