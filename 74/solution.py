from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def find(nums, target, left, right):
            if left >= right:
                return right
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    return find(nums, target, left, mid-1)
                elif nums[mid] < target:
                    return find(nums, target, mid+1, right)
                else:
                    return mid

        # 先找行
        r_nums = [matrix[i][-1] for i in range(m)]
        index_i = find(r_nums, target, 0, m-1)
        if index_i < 0:
            index_i = 0
        if index_i > m-1:
            index_i = m-1
        if matrix[index_i][-1] == target:
            print(index_i, -1)
            return True
        else:
            if matrix[index_i][-1] < target:
                index_i += 1
                if index_i > m-1:
                    return False
        # 再找列
        index_j = find(matrix[index_i], target, 0, n-1)
        if matrix[index_i][index_j] == target:
            #print(index_i, index_j)
            return True
        return False

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 60]]
    target = 61
    #输出：true


    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    #输出：false

    matrix = [[2, 4]]
    target = 5

    matrix = [[2], [4]]
    target = 3

    matrix = [[-8, -7, -5, -3, -3, -1, 1], [2, 2, 2, 3, 3, 5, 7], [8, 9, 11, 11, 13, 15, 17], [18, 18, 18, 20, 20, 20, 21],
     [23, 24, 26, 26, 26, 27, 27], [28, 29, 29, 30, 32, 32, 34]]
    target = -5


    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    print(result)