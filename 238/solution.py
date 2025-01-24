from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 不使用除法
        if not nums:
            return nums
        acc_multi_r2l = []
        m = 1
        for n in nums[::-1]:
            m *= n
            acc_multi_r2l.append(m)
        nums_len = len(nums)
        m = 1
        result = []
        for i in range(nums_len):
            index = nums_len-i-2
            if index >=0:
                result.append(m*acc_multi_r2l[index])  # nums_len - 2
            else:
                result.append(m)
            m *= nums[i]
        return result

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    #输出: [24, 12, 8, 6]

    # nums = [-1, 1, 0, -3, 3]
    # #输出: [0, 0, 9, 0, 0]

    solution = Solution()
    result = solution.productExceptSelf(nums)
    print(result)