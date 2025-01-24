from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        most_right = 0
        step_count = 0
        for index, steps in enumerate(nums):
            if index > most_right:
                return False
            if most_right >= target:
                return step_count
            if index + steps > most_right:
                most_right = max(most_right, index + steps)
                step_count += 1

if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    # # 输出: 2

    # nums = [2, 3, 0, 1, 4]
    # #输出: 2

    # nums = [2, 1]
    # #1

    # nums = [1,2,1,1,1]
    # # 3

    nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    # 2


    solution = Solution()
    result = solution.jump(nums)
    print(result)