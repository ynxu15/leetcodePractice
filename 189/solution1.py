from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        nums_len = len(nums)
        # 位置变换 i -> i+k % nums_len
        k = k % nums_len
        nums[nums_len-k:], nums[:nums_len-k] = nums[:nums_len-k], nums[nums_len-k:]


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]  # [5,6,7,1,2,3,4]
    # k = 3

    nums = [-1, -100, 3, 99]  # [3,99,-1,-100]
    k = 2


    solution = Solution()
    result = solution.rotate(nums, k)
    print(nums)