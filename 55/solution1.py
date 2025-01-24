from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        stack = [0]
        target = len(nums) - 1
        checked_set = set()
        while stack:
            index = stack.pop()
            if index == target:
                return True
            checked_set.add(index)
            steps = nums[index]
            for s in range(1, steps+1):
                next_index = index + s
                if next_index <= target and next_index not in checked_set:
                    stack.append(next_index)

        return False


if __name__ == '__main__':
    #nums = [2, 3, 1, 1, 4]
    #输出：true

    # nums = [3, 2, 1, 0, 4]
    # #输出：false

    nums = [1, 1, 1, 0]
    # True

    solution = Solution()
    result = solution.canJump(nums)
    print(result)