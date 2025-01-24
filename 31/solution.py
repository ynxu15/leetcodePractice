from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums

        # 要从右向左，判断各个子数组能否找到下一个数字，如果找到则返回
        # 每个子数组判断有下一个数的规则是，对当前最左的那个数，向右侧找比它大的最小数，如果存在，则交换两个数的位置，然后对剩余的数进行从小到大排序即可。
        #

        def find(left, right, num, nums):
            # 从左向右是降序排序
            l, r = left, right
            # 二分法查找
            while l < r:
                mid = (l+r)//2
                if nums[mid] > num:
                    l = mid + 1
                elif nums[mid] < num:
                    r = mid - 1
                else: # 相等的情况
                    r = mid - 1

            if nums[l] > num:
                return l
            elif nums[l] <= num and l > left:
                return l - 1
            return -1

        findFlag = False
        for i in range(len(nums)-1, 0, -1):
            # 排序
            #nums[i:] = sorted(nums[i:])
            # 然后看下一个数, 从排序结果中，找到比它大的最小数
            index = find(i, len(nums)-1, nums[i-1], nums)
            # 交换
            if index > 0:
                nums[i-1], nums[index] = nums[index], nums[i-1]
                findFlag = True
                nums[i:] = list(reversed(nums[i:]))
                break

        if not findFlag:
            nums.sort()
        return nums

if __name__ == '__main__':
    #nums = [1, 2, 3]
    # 输出：[1, 3, 2]
    #
    nums = [3, 2, 1]
    # # 输出：[1, 2, 3]
    #
    #nums = [1, 1, 5]
    # 输出：[1, 5, 1]

    #nums = [1]

    #nums = [2, 1, 3, 2]

    nums = [1,3,2]

    nums = [2, 3, 1]

    nums = [5,4,7,5,3,2]

    solution = Solution()
    result = solution.nextPermutation(nums)
    print(result)