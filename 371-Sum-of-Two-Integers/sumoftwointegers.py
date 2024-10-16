class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        result = ''
        carry = False
        for i in range(-1, -1 * max(len(a), len(b)) - 2, -1):
            current = 0
            if carry:
                current += 1
            if len(a) >= (-1 * i) and a[i] == '1':
                current += 1
            if len(b) >= (-1 * i) and b[i] == '1':
                current += 1
            result = str(current % 2) + result
            carry = current // 2 != 0
        return int(result, 2)