from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0]*2 for _ in range(N)]
        for i in range(N):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -prices[0]
            elif i == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) # 继续空仓，或者今天卖出股票
                dp[i][1] = max(dp[i-1][1], -prices[i])  # 继续持有股票，或者今天买入股票
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) # 继续空仓，或者今天卖出股票
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i]) # 继续持有股票，或者买入股票
        return dp[-1][0]

if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    # 3

    prices = [1]
    # 0

    prices = [1, 2]
    # 1

    prices = [1, 2, 4]
    # 3

    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)