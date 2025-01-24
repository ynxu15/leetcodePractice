from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1_len, t2_len = len(text1), len(text2)
        if t1_len == 0 or t2_len == 0:
            return 0
        dp = [[0] * (t2_len+1) for _ in range(t1_len+1)]
        for i in range(1, t1_len+1):
            for j in range(1, t2_len+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    # 输出：3


    # text1 = "abc"
    # text2 = "abc"
    # # 输出：3


    # text1 = "abc"
    # text2 = "def"
    # # 输出：0


    solution = Solution()
    result = solution.longestCommonSubsequence(text1, text2)
    print(result)