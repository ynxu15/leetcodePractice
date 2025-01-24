from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permuteHelp(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            result = []
            for i in range(len(nums)):
                nums_tmp = [nums[j] for j in range(len(nums))]
                del nums_tmp[i]
                rs = permuteHelp(nums_tmp)
                for r in rs:
                    #result.append([nums[i]]+r)
                    result.append(r+[nums[i]])
            return result
        return permuteHelp(nums)

if __name__ == '__main__':
    nums = [1, 2, 3]
    # 输出：[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    # nums = [0, 1]
    # # 输出：[[0, 1], [1, 0]]
    #
    # nums = [1]
    # # 输出：[[1]]

    solution = Solution()
    result = solution.permute(nums)
    print(result)