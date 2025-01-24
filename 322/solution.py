from typing import List

'''
位图+dp解决 
dp[i][j] 表示使用i+1个硬币之后，能不能达到j这个amount
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def printBi(n):
            for i in range(amount+1):
                print(n>>i&1, end=' ')

        if not coins or amount < 0:
            return -1
        if amount == 0:
            return 0
        smallest = min(coins)
        N = amount//smallest + 1
        t = 1 << amount
        # printBi(t)
        # print()
        for i in range(N):
            tmp = 0
            for c in coins:
                tmp |= t >> c
            t |= tmp
            # print(i, ' >> ', end='')
            # printBi(t)
            # print()
            if t & 1 == 1:
                return i + 1
        return -1

    # def coinChange2(self, coins: List[int], amount: int) -> int:
    #     if not coins or amount < 0:
    #         return -1
    #     if amount == 0:
    #         return 0
    #     smallest = min(coins)
    #     N = amount//smallest + 1
    #     t = 1 << amount
    #     for i in range(N):
    #         for c in coins:
    #             t |= t >> c
    #     return t & 1 == 1


if __name__ == '__main__':
    # coins = [1, 2, 5]
    # amount = 11
    # # 输出：3
    # # 解释：11 = 5 + 5 + 1

    # coins = [2]
    # amount = 3
    # # 输出：-1

    # coins = [1]
    # amount = 0
    # # 输出：0

    solution = Solution()
    result = solution.coinChange(coins, amount)
    print(result)