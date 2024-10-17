class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask. Expressed in hexadecimal
        mask = 0xffffffff

        while (b & mask) > 0:
            add = a ^ b
            carry = (a & b) << 1
            a = add
            b = carry
        return (a & mask) if b > 0 else a