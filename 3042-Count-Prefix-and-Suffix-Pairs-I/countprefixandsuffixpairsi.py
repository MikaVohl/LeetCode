from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count
        
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        k = len(str1)
        if len(str2) < k:
            return False
        return str2.startswith(str1) and str2.endswith(str1)