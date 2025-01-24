from typing import List
'''
O(1)空间完成
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 不使用除法
        if not nums:
            return nums

        nums_len = len(nums)
        result = [0] * nums_len
        m = 1
        # 搞定左边的乘积
        for i in range(nums_len):
            result[i] = m
            m *= nums[i]

        # 搞定右边的乘积
        m = 1
        for i in range(nums_len-1, -1, -1):
            result[i] *= m
            m *= nums[i]

        return result

if __name__ == '__main__':
    # nums = [1, 2, 3, 4]
    # #输出: [24, 12, 8, 6]

    nums = [-1, 1, 0, -3, 3]
    #输出: [0, 0, 9, 0, 0]

    solution = Solution()
    result = solution.productExceptSelf(nums)
    print(result)