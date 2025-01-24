from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:  # 说明这一段是有序的，直接返回最小的left
                return nums[left]
            else:
                if nums[mid] < nums[left]:
                    right = mid
                else:
                    left = mid + 1
        return nums[left]

if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    #输出：1

    nums = [4, 5, 6, 7, 0, 1, 2]
    #输出：0

    nums = [11, 13, 15, 17]
    #输出：11


    solution = Solution()
    result = solution.findMin(nums)
    print(result)