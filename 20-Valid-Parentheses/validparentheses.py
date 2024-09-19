class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            # closing braces are always 1 or 2 ascii values larger than the opening brace
            if len(stack) > 0 and (ord(stack[-1]) == ord(letter) - 1 or ord(stack[-1]) == ord(letter) - 2):
                stack.pop()
            else:
                stack.append(letter)
        return not stack
    
print(Solution().isValid("()"))