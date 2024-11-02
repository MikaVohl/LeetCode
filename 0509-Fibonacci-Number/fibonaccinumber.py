# Time Complexity: O(2^n)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n < 2: return n
#         return self.fib(n-1) + self.fib(n-2)

# Time Complexity: O(n)
computations = {}

class Solution:
    def fib(self, n:int) -> int:
        if n < 2: return n
        if n in computations:
            return computations[n]
        result = self.fib(n-1) + self.fib(n-2)
        computations[n] = result
        return result