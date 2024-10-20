# String manipulation method
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         return int(''.join(reversed(format(n, '0>32b'))), 2)

# Bit manipulation method
class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for _ in range(32):
            output <<= 1 # shift output bits to the left
            output ^= (n & 1) # set the last bit of output to the last bit of n
            n >>= 1 # shift bits in n to the right
        return output