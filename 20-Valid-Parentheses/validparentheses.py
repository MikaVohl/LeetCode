class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for letter in s:
            if stack and letter == pairs[stack[-1]]:
                stack.pop()
            else:
                if letter not in pairs:
                    return False
                stack.append(letter)
        return not stack
    
print(Solution().isValid("()"))