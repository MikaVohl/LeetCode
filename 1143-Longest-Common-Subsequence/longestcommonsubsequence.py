class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0] * len(text2) for _ in range(len(text1)) ]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if i == 0:
                    dp[i][j] = int(text1[0] in text2[:j+1])
                elif j == 0:
                    dp[i][j] = int(text2[0] in text1[:i+1])
                elif text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]