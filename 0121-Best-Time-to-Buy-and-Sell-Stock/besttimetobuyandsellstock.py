from typing import List

# Time Complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            if price > min_price:
                profit = max(price - min_price, profit)
        return profit