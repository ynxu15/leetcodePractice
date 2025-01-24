from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def getSubsets(nums, first=0):
            if first == n:
                return [[]]
            if first < n:
                rs = getSubsets(nums, first+1)
                result = []
                for r in rs:
                    result.append(r)
                    result.append([nums[first]]+r)
                return result
        return getSubsets(nums)

if __name__ == '__main__':
    nums = [1, 2, 3]
    #输出：[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    # nums = [0]
    # #输出：[[], [0]]

    solution = Solution()
    result = solution.subsets(nums)
    print(result)