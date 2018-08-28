class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        best_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > best_profit:
                best_profit = p - min_price
        return best_profit
