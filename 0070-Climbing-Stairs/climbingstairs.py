# Recursive approach. Exceeds time limit
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# Recursive approach with memoization to optimize time.
memo = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        memo[n] = result
        return result

