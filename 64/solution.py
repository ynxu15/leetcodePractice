from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # 输出：7
    # 解释：因为路径 1→3→1→1→1 的总和最小。

    # grid = [[1, 2, 3], [4, 5, 6]]
    # # 输出：12

    grid = [[1]]

    solution = Solution()
    result = solution.minPathSum(grid)
    print(result)