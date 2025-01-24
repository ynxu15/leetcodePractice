from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''广度优先遍历'''

        m, n = len(grid), len(grid[0])

        bad_set = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bad_set.add((i, j))

        minute = 0
        while len(bad_set)>0:
            new_set = set()
            findFlag = False
            for i,j in bad_set:
                if i>0 and grid[i-1][j] == 1:
                    grid[i - 1][j] = 2
                    new_set.add((i-1, j))
                    findFlag = True
                if j>0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    new_set.add((i, j-1))
                    findFlag = True
                if i<m-1 and grid[i+1][j] == 1:
                    grid[i + 1][j] = 2
                    new_set.add((i+1, j))
                    findFlag = True
                if j<n-1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    new_set.add((i, j+1))
                    findFlag = True
            bad_set = new_set
            if findFlag:
                minute += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minute


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # 输出：4

    # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    # # 输出：-1

    # grid = [[0, 2]]
    # # 输出：0

    grid = [[0]]

    solution = Solution()
    result = solution.orangesRotting(grid)
    print(result)