from typing import List

'''
O(N)
快排，获得第K大的值
'''
class Solution:

    def quick_sort(self, nums, left_index, right_index):
        if left_index == right_index:
            return left_index
        mid_num = nums[left_index]
        l, r = left_index+1, right_index
        while l < r:
            if nums[l] > mid_num:
                # 交换
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        if nums[left_index] > nums[l]:
            nums[l], nums[left_index] = nums[left_index], nums[l]
        return l

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        if k > len(nums):
            return None

        nums_len = len(nums)
        left, right = 0, len(nums)-1
        while left <= right:
            if left == right and nums_len - left == k:
                return nums[left]
            mid = self.quick_sort(nums, left, right)
            if nums_len - mid >= k:
                left = mid
            else:
                right = mid-1
        return 0


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    #输出: 5

    # nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # k = 4
    # # 输出: 4

    solution = Solution()
    result = solution.findKthLargest(nums, k)
    print(result)