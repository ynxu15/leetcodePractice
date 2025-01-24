from typing import List

'''
深度优先遍历
'''
class Solution:
    def check(self, nums, checked, index, target):
        checked[index] = 1
        steps = nums[index]
        if index + steps >= target:
            return True

        for s in range(1, steps+1):
            if index + s <= target and checked[index+s] == 0:
                result = self.check(nums, checked, index+s, target)
                if result:
                    return result
            if index - s >= 0 and checked[index-s] == 0:
                result = self.check(nums, checked, index-s, target)
                if result:
                    return result
        #checked[index] = 0
        return False

    def canJump(self, nums: List[int]) -> bool:
        checked = [0] * len(nums)
        return self.check(nums, checked, 0, len(nums)-1)


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