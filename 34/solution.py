from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def search(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[left] < target:
                        left += 1
                    elif nums[right] > target:
                        right -= 1
                    else:
                        return [left, right]
            return [-1, -1]

        def search2(nums, left, right, target):
            '''递归调用'''
            if left > right:
                return [-1, -1]
            mid = (left + right) // 2
            if nums[mid] < target:
                return search2(nums, mid+1, right, target)
            elif nums[mid] > target:
                return search2(nums, left, mid-1, target)
            else:  # 相等的情况，切分开测试
                if nums[left] == target:
                    if nums[right] == target:
                        return [left, right]
                    else:
                        # 检索 [mid, right] 区间
                        result = search2(nums, mid, right-1, target)
                        # 合并区间
                        return [left, result[1]]
                elif nums[right] == target:
                    # 检索 [mid, right] 区间
                    result = search2(nums, left+1, mid, target)
                    # 合并区间
                    return [result[0], right]
                else:  # 两边都不等，只有中间是相等的，则两边分别二分查找，然后合并
                    result1= search2(nums, left, mid-1, target)
                    result2= search2(nums, mid, right, target)
                    if result1[0] == -1:
                        return result2
                    else:
                        return [result1[0], result2[1]]
            return [-1, -1]

        #return search(nums, 0, len(nums)-1, target)

        return search2(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    # 输出：[3, 4]

    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6
    # # 输出：[-1, -1]

    # nums = []
    # target = 0
    # # 输出：[-1, -1]


    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)