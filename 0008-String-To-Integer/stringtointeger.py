class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1 if s[0] != '-' else -1
        number = 0
        if s[0] == '-' or s[0] == '+': s = s[1:]
        for i in range(len(s)):
            if s[i] == '0' and number == 0: continue
            if s[i] < '0' or s[i] > '9':
                break
            number = number * 10 + int(s[i])
        number = number * sign
        return max(min(2**31 - 1, number), -2**31)