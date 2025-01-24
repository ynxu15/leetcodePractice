from typing import List
class Solution:
    def longestPalindrome2(self, s: str) -> str:
        # 插入特殊字符
        target_list = []
        for c in s:
            target_list.append('|')
            target_list.append(c)
        target_list.append('|')

        dp = [1] * len(target_list)
        max_len = 0
        max_index = -1
        for i in range(1, len(target_list)):
            left_index = i - dp[i-1] - 1
            if left_index < 0:
                continue
            if target_list[i] == target_list[left_index]:
                dp[i] = dp[i-1]+2
                if dp[i] > max_len:
                    max_len = dp[i]
                    max_index = i
        ans = []
        for i in range(max_index-dp[max_index]+1, max_index+1):
            if target_list[i]!= '|':
                ans.append(target_list[i])
        return ''.join(ans)


    def longestPalindrome(self, s: str) -> str:
        # 插入特殊字符
        dp = [[1, 0] for _ in range(len(s))]
        # dp[i][0] 奇数的队列长度
        # dp[i][1] 偶数的队列长度
        max_len1, max_len2 = 1, 0
        max_index1, max_index2 = 0, 0
        for i in range(1, len(s)):
            # 处理奇数的情况
            left_index = i - dp[i - 1][0] - 1
            if left_index >= 0:
                if s[left_index] == s[i]:
                    dp[i][0] = dp[i-1][0] + 2
                    if max_len1 < dp[i][0]:
                        max_len1 = dp[i][0]
                        max_index1 = i

            # 处理偶数队列长度
            left_index = i - dp[i - 1][1] - 1
            if left_index >= 0:
                if s[left_index] == s[i]:
                    dp[i][1] = dp[i-1][1] + 2
                    if max_len2 < dp[i][1]:
                        max_len2 = dp[i][1]
                        max_index2 = i
        if max_len1 > max_len2:
            return s[max_index1 - dp[max_index1][0]+1: max_index1+1]
        else:
            return s[max_index2 - dp[max_index2][1] + 1: max_index2 + 1]




if __name__ == '__main__':
    s = "babad"

    # s = "cbbd"
    # # 输出："bb"

    s = "a"

    s = "aaaa"

    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)