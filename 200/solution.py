from typing import List

class Solution:
    def numIslands2(self, grid: List[List[str]]) -> int:
        '''错的'''
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        head = [[(i, j) for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 找在同一个岛上的，修改为同一个head
                    if i > 0 and grid[i-1][j] == '1':  # 修改这个grid的头，指向当前节点
                        h1 = head[i-1][j]
                        head[i][j] = h1
                        if j > 0 and grid[i][j-1] == '1':  # 修改这个方向上的所有节点为 （ii,jj）
                            h2 = head[i][j-1]
                            if h2 != h1:
                                head[i][j - 1] = h1
                                ht = h2
                                while head[ht[0]][ht[1]] != ht:
                                    htt = head[ht[0]][ht[1]]
                                    head[ht[0]][ht[1]] = h1
                                    ht = htt
                                head[ht[0]][ht[1]] = h1

                    elif j > 0 and grid[i][j-1] == '1':
                        head[i][j] = head[i][j-1]
                else:
                    head[i][j] = (-1, -1)
        #print(head)
        ans = 0
        for i in range(m):
            for j in range(n):
                if head[i][j] == (i, j):
                    ans += 1
                    #print(i, j)
        return ans

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count



if __name__ == '__main__':
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    # #输出：1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    #输出：3

    grid = \
    [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
     ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1"],
     ["0", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
     ["1", "1", "0", "1", "1", "0", "0", "0", "0", "1"],
     ["1", "0", "1", "0", "1", "0", "0", "1", "0", "1"],
     ["1", "0", "0", "1", "1", "1", "0", "1", "0", "0"],
     ["0", "0", "1", "0", "0", "1", "1", "1", "1", "0"],
     ["1", "0", "1", "1", "1", "0", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
     ["1", "0", "1", "1", "1", "1", "1", "1", "1", "0"]]

    solution = Solution()
    result = solution.numIslands(grid)
    print(result)