from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0]*2 for _ in range(N)]
        # dp[i][0] 表示不偷i的情况下，能获得的最高金额
        # dp[i][1] 表示偷i的情况下，能获得最高金额
        dp[0][1] = nums[0]
        for i in range(1, N-1):
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            dp[i][1] = max(dp[i-2][1]+nums[i], dp[i-1][0]+nums[i])
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
        dp[i][1] = max(dp[i - 2][1] + nums[i], dp[i - 1][0] + nums[i])

if __name__ == '__main__':
    nums = [2, 3, 2]
    #输出：3

    nums = [1, 2, 3, 1]
    #输出：4

    nums = [1, 2, 3]
    #输出：3

    solution = Solution()
    result = solution.rob(nums)
    print(result)