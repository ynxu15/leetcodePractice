from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int], cooldown, fee) -> int:
        '''
        :param k:  最多K笔交易
        :param prices:  每天的价格
        :param cooldown: 冷静期，卖完买入要间隔的天数
        :param fee: 交易费
        :return:
        '''
        if not prices:
            return 0
        N = len(prices)
        if k > N // 2:
            return self.maxProfilt_k_inf(prices, cooldown, fee)
        dp = [[[0]*2 for __ in range(k+1)] for _ in range(N)]

        for i in range(N):
            dp[i][0][1] = -1000000
            dp[i][0][0] = 0

        for i in range(N):
            for j in range(1, k+1):  # 这里有个潜台词，dp[i][0][0] = 0  dp[i][0][1] = 0  没有交易的情况，初始值都是0，不用更新。
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i] - fee
                    continue

                if i - cooldown - 1 == -1:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][k][1]+prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], -prices[i]-fee)
                    continue


                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])    # 继续空仓，或者今天卖出股票
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-cooldown-1][0]-prices[i]-fee)  # 继续持有股票，或者买入股票
        return dp[-1][-1][0]

    def maxProfilt_k_inf(self, prices: List[int], cooldown, fee) -> int:
        '''
        :param prices:  每天的价格
        :param cooldown: 冷静期，卖完买入要间隔的天数
        :param fee: 交易费
        :return:
        '''
        N = len(prices)
        dp = [[0]*2 for _ in range(N)]

        for i in range(N):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
                continue

            if i-cooldown-1 == -1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i - 1][1], -prices[i]-fee)
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])    # 继续空仓，或者今天卖出股票
                dp[i][1] = max(dp[i-1][1], dp[i-cooldown-1][0]-prices[i]-fee)  # 继续持有股票，或者买入股票
        return dp[-1][0]

if __name__ == '__main__':
    # k = 2
    # prices = [2, 4, 1]
    # #输出：2
    #
    # # k = 2
    # # prices = [3, 2, 6, 5, 0, 3]
    # # # 7
    #
    # k = 2
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # # 6
    #
    # solution = Solution()
    # result = solution.maxProfit(k, prices)
    # print(result)
    pass