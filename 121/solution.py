from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0]*2 for _ in range(N)]
        # 0 手上没有股票， 1 手上有股票
        # dp[i][j][0] 第i天，第j次交易，手上没有股票，赚了多少钱
        # dp[i][j][1] 第i天，第j次交易，手上有股票，赚了多少钱
        for i in range(0, N):
            if i-1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i-1][0], prices[i] + dp[i-1][1])  # 继续空着，或者今天卖出，得到收益
                dp[i][1] = max(dp[i-1][1], -prices[i])  # 今天买入的收益 或者 继续持有股票的收益

        return dp[-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        ans = 0
        min_num, max_num = 10000, -10000
        for p in prices:
            if min_num>p:
                min_num = p
                max_num = p
            if max_num < p:
                max_num = p
            if ans < max_num - min_num:
                ans = max_num - min_num
        return ans

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    # 5

    prices = [7,6,4,3,1]
    # 0

    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)