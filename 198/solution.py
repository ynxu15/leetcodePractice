from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        helps = [[0]*2 for _ in range(len(nums))]
        # [i][0] 不包括i的时候的最大值
        # [i][1] 包括i的时候的最大值
        helps[0][1] = nums[0]
        for i in range(1, len(nums)):
            helps[i][0] = max(helps[i-1][0], helps[i-1][1])
            helps[i][1] = helps[i-1][0]+nums[i]
        return max(helps[-1])

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    # 输出：4

    # nums = [2, 7, 9, 3, 1]
    # # 输出：12

    # nums = [1, 1]

    solution = Solution()
    result = solution.rob(nums)
    print(result)