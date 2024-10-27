class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [ 0 for _ in range(26)]
        freq2 = [ 0 for _ in range(26)]

        for i in range(max(len(s), len(t))):
            if i >= len(s) or i >= len(t):
                return False
            freq1[ord(s[i]) - 97] += 1
            freq2[ord(t[i]) - 97] += 1
        
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True