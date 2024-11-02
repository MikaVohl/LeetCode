from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, number in enumerate(nums):
            if number in differences:
                return differences[number], i
            differences[target - number] = i