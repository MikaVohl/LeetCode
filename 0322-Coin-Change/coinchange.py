from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(coins, amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            results = []
            for coin in coins:
                if coin <= amount:
                    result = helper(coins, amount - coin)
                    if result != -1:
                        results.append(1 + result)
            minimum = min(float('inf'), *results) if len(results) > 0 else -1
            memo[amount] = minimum
            return minimum
        return helper(coins, amount)