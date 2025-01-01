class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        ptr1 = 0
        ptr2 = len(number) - 1
        while ptr1 < ptr2:
            if number[ptr1] != number[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
        return True