from typing import List

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        most_right = 0
        target = len(nums)-1
        for index, steps in enumerate(nums):
            if index > most_right:
                return False
            if most_right >= target:
                return True
            most_right = max(most_right, index+steps)


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    #输出：true

    # nums = [3, 2, 1, 0, 4]
    # #输出：false

    # nums = [1, 1, 1, 0]
    # # True

    solution = Solution()
    result = solution.canJump(nums)
    print(result)