from typing import List

# Sliding window technique. This yields O(n^2) time complexity which is too long for this problem
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         total = nums[0]
#         for i in range(1, len(nums)+1): # window size
#             for j in range(len(nums) - i + 1):
#                 total = max(total, sum(nums[j:j+i]))
#         return total

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_best = 0
        total_best = float('-inf')
        for num in nums:
            current_best = max(current_best + num, num) # If the current num must be included, determine if its better to include the last number or not
            total_best = max(total_best, current_best)
        return total_best