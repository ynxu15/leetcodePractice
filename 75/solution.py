from typing import List


class Solution:
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''双指针解决'''
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] == 0:   # 不用修改
                left += 1
            elif nums[left] == 1:  # 左边不动
                if nums[right] == 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                elif nums[right] == 2:
                    right -= 1
                else: # 左右两侧都是1的情况，那要找一个0放在当前这个地方
                    find_flag = False
                    for i in range(left+1, right):
                        if nums[i] == 0 or nums[i] == 2:
                            nums[left], nums[i] = nums[i], nums[left]
                            find_flag = True
                    if not find_flag:
                        return nums

            else:  # 左边是2，找到一个右侧是1的或者0的交换位置
                if nums[right] == 2:
                    right -= 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
        return nums

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''三指针解决'''
        nums_len = len(nums)
        left, i, right = 0, 0, len(nums)-1
        # left 是0的最右侧， right 是2 的最左侧，中间是1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    # 输出：[0, 0, 1, 1, 2, 2]


    #nums = [2, 0, 1]
    # 输出：[0, 1, 2]

    #nums = [0, 1, 2, 0, 1, 2]

    solution = Solution()
    result = solution.sortColors(nums)
    print(result)