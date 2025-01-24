from typing import List

'''
常量空间
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len, col_len = len(matrix), len(matrix[0])
        zero_row_set = 0
        zero_col_set = 0
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    zero_row_set = zero_row_set | 1 << i
                    zero_col_set = zero_col_set | 1 << j

        # 打印
        # for i in range(row_len-1, -1, -1):
        #     print(zero_row_set >> i & 1, end=' ')
        # print()
        # for j in range(col_len-1, -1, -1):
        #     print(zero_col_set >> j & 1, end=' ')
        # print()

        # 设置为0
        for i in range(row_len):
            if zero_row_set >> i & 1 == 1:
                matrix[i] = [0] * col_len

        for j in range(col_len):
            if zero_col_set >> j & 1 == 1:
                for i in range(row_len):
                    matrix[i][j] = 0



if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # 输出：[[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # # 输出：[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    solution = Solution()
    result = solution.setZeroes(matrix)
    print(matrix)