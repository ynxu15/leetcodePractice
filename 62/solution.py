from typing import List
class Solution:
    def uniquePaths2(self, m: int, n: int) -> int:
        '''按照步骤来更新dp'''
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for step in range(1, m+n-1):
            for i in range(step+1):  # 横着走i 步
                if i >= m:
                    continue
                j = step - i  # 纵向走j步
                if j >= n:
                    continue
                if i <= 0:
                    dp[i][j] = dp[i][j-1]
                elif j<= 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    m = 3
    n = 7
    # 输出：28


    # m = 3
    # n = 2
    # # 输出：3
    # # 解释：
    # # 从左上角开始，总共有 3 条路径可以到达右下角。
    # # 1. 向右 -> 向下 -> 向下
    # # 2. 向下 -> 向下 -> 向右
    # # 3. 向下 -> 向右 -> 向下

    # m = 7
    # n = 3
    # # 输出：28

    # m = 3
    # n = 3
    # # 输出：6

    solution = Solution()
    result = solution.uniquePaths(m, n)
    print(result)