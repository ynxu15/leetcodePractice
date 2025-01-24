from typing import List

'''
前缀和+字典的优化
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        s = 0
        nums_len = len(nums)
        accumulate_sum_map = {0: 1}  # acc_sum: count
        ans = 0
        for i in range(nums_len):
            s += nums[i]
            l = s - k
            if l in accumulate_sum_map:
                ans += accumulate_sum_map[l]
            if s in accumulate_sum_map:
                accumulate_sum_map[s] += 1
            else:
                accumulate_sum_map[s] = 1
        return ans

if __name__ == '__main__':
    nums = [1,1,1]
    k = 2   # 输出2

    nums = [1,2,3]
    k = 3  # 输出2

    solution = Solution()
    result = solution.subarraySum(nums, k)
    print(result)