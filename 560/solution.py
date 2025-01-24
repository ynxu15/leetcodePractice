from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        accumulate_sum = [0]*len(nums)
        s = 0
        nums_len = len(nums)
        for i in range(nums_len):
            s += nums[i]
            accumulate_sum[i] = s

        accumulate_sum.insert(0, 0)
        ans = 0
        # 看从(i-j]是否和等于k
        for i in range(0, nums_len):
            for j in range(i+1, nums_len+1):
                s = accumulate_sum[j] - accumulate_sum[i]
                if s == k:
                    ans += 1
        return ans

if __name__ == '__main__':
    nums = [1,1,1]
    k = 2   # 输出2

    # nums = [1,2,3]
    # k = 3  # 输出2

    solution = Solution()
    result = solution.subarraySum(nums, k)
    print(result)