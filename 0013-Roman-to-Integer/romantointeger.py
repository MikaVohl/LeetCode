class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i, char in enumerate(s):
            if i < len(s) - 1 and lookup[char] < lookup[s[i+1]]:
                total -= lookup[char]
            else:
                total += lookup[char]
        return total