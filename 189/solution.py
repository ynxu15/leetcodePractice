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
        moved_set = set()
        processed_set = set()
        for i in range(nums_len):
            if i in moved_set:
                continue
            moved_set.add(i)

            j = (i+k) % nums_len
            if i == j:
                processed_set.add(j)
                continue
            source_num = nums[i]
            while j not in processed_set:
                tmp = nums[j]
                nums[j] = source_num
                source_num = tmp
                moved_set.add(j)
                processed_set.add(j)
                j = (j+k) % nums_len


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]  # [5,6,7,1,2,3,4]
    # k = 3

    nums = [-1, -100, 3, 99]  # [3,99,-1,-100]
    k = 2


    solution = Solution()
    result = solution.rotate(nums, k)
    print(nums)