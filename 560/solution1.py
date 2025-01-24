from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        accumulate_sum = [0]*len(nums)
        s = 0
        nums_len = len(nums)
        accumulate_sum_map = {0: set([-1])}
        for i in range(nums_len):
            s += nums[i]
            accumulate_sum[i] = s
            if s in accumulate_sum_map:
                accumulate_sum_map[s].add(i)
            else:
                accumulate_sum_map[s] = set([i])

        ans = 0
        # 看从(j-i]是否和等于k
        # 检查需要的和是否在字典中
        # 计算结果的时候，需要1）去掉当前位置自己 2) 去掉大于自己的index 防止重复计算
        for i in range(nums_len):
            l = accumulate_sum[i] - k
            if l in accumulate_sum_map:
                for j in accumulate_sum_map[l]:
                    if j < i:
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