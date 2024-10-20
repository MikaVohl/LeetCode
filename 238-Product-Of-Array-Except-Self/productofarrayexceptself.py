from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        suffix = 1
        for num in nums:
            output.append(prefix)
            prefix *= num
        for i in range(len(nums) - 1, 0, -1):
            output[i] *= suffix
            suffix *= nums[i]
        output[0] *= suffix
        return output