from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        def searchHelp1(nums, left, right, target):
            if left > right:
                return -1
            if left == right and nums[left] == target:
                return left

            mid = (left+right)//2
            if nums[mid] < nums[left]: # 说明  【left, mid】区间是旋转的
                result1 = searchHelp(nums, left, mid, target)
                result2 = searchHelp(nums, mid+1, right, target)
                return max(result1, result2)
            elif nums[mid] > nums[right]: # 说明 [mid, right]区间是旋转的
                result1 = searchHelp(nums, left, mid, target)
                result2 = searchHelp(nums, mid+1, right, target)
                return max(result1, result2)
            else: # 正常的二分查找
                if nums[mid] < target:
                    return searchHelp(nums, mid+1, right, target)
                elif nums[mid] > target:
                    return searchHelp(nums, left, mid-1, target)
                else:
                    return mid
        def searchHelp(nums, left, right, target):
            if left > right:
                return -1
            if left == right and nums[left] == target:
                return left

            mid = (left+right)//2
            if nums[mid] < nums[left]: # 说明  【left, mid】区间是旋转的

                if nums[mid] > target:
                    return searchHelp(nums, left, mid-1, target)
                else:
                    return searchHelp(nums, mid+1, right, target)
            elif nums[mid] > nums[right]:  # 说明 [mid, right]区间是旋转的
                if nums[mid] > target:
                    return searchHelp(nums, left, mid-1, target)
                else:
                    return searchHelp(nums, mid+1, right, target)
            else: # 正常的二分查找
                if nums[mid] < target:
                    return searchHelp(nums, mid+1, right, target)
                elif nums[mid] > target:
                    return searchHelp(nums, left, mid-1, target)
                else:
                    return mid

        return searchHelp(nums, 0, len(nums)-1, target)

if __name__ == '__main__':

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    # 输出：4

    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 3
    # # 输出：-1


    # nums = [1]
    # target = 0
    # # 输出：-1


    solution = Solution()
    result = solution.search(nums, target)
    print(result)