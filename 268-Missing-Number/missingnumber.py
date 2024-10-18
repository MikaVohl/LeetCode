from typing import List
from functools import reduce

# Slow, brute force solution:
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i in range(0, len(nums)+1):
#             if i not in nums:
#                 return i

# Solution using property of arithmetic sequence
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         expected_sum = (n * (n+1)) // 2 # Sum of numbers from 0-n
#         actual_sum = sum(nums)
#         return expected_sum - actual_sum
    
# Solution using bit manipulation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        combined = list(range(len(nums) + 1)) + nums
        result = combined[0]
        for i in range(1, len(combined)):
            result = result ^ combined[i]
        return result
    
# Tweaked solution with reduce function
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         combined = list(range(len(nums) + 1)) + nums
#         return reduce(lambda x, y: x ^ y, combined)