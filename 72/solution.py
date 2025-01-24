from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_len, w2_len = len(word1), len(word2)
        if w1_len == 0:
            return w2_len
        if w2_len == 0:
            return w1_len

        dp = [[0] * (w2_len) for _ in range(w1_len)]
        if word1[0] == word2[0]:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for i in range(1, w1_len):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i-1][0]+1
        for j in range(1, w2_len):
            if word1[0] == word2[j]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j-1]+1
        for i in range(1, w1_len):
            for j in range(1, w2_len):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    #输出：3


    word1 = "intention"
    word2 = "execution"
    # #输出：5


    solution = Solution()
    result = solution.minDistance(word1, word2)
    print(result)