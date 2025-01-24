from typing import Optional, List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        dp = [-1]*len(s)  # dp 存储的是当前字符为 （ 时候，向右最大能到的合规括号）的下标
        for i in range(len(s)-1):
            if s[i] == '(' and s[i+1] == ')':
                dp[i] = i+1
                #dp[i+1] = i

        findFlag = True
        while findFlag:
            findFlag = False
            i = 0
            while i < len(s):
                if s[i] == '(' and dp[i] >= 0: # 找到对应的了
                    next_step = dp[i]+1
                    if next_step < len(s) and dp[next_step] >= 0: # 如何有相邻的两个有效区间，则合并
                        dp[i] = dp[next_step]
                        findFlag = True
                    if i > 0 > dp[i - 1] and dp[i] < len(s)-1 and s[i - 1] == '(' and s[dp[i] + 1] == ')':
                        findFlag = True
                        dp[i-1] = dp[i]+1
                        i = dp[i-1] + 1
                    else:
                        i = dp[i] + 1
                else:
                    i += 1


        max_count = 0
        i = 0
        while i < len(s):
            if dp[i] >=0:
                max_count = max(max_count, dp[i] - i +1)
                i = dp[i]+1
            else:
                i += 1
        return max_count

if __name__ == '__main__':
    # s = "(()"
    # #输出：2

    s = ")()())"
    #输出：4

    # s = ""
    # #输出：0

    print(Solution().longestValidParentheses(s))