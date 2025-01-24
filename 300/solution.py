from typing import List

'''
后续可以修改为递归的方式做
'''

class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        '''动态规划算法'''
        if not nums:
            return 0

        ans = []
        nums_len = len(nums)
        dp = [0] * nums_len  # dp[i] 是以第i个元素结尾的最长递增子序列的长度
        dp[0] = 1
        sort_indexs = [0]  # 按照nums值排序的下标，从小到大
        # 先按照dp值排序，如果dp值相同，按照nums值从小到大排序
        # 每次从排头开始比较，找到第一个比nums[j]小的数即可。
        def findMax(n):
            '''查询不大于n的元素的下标'''
            for i in sort_indexs:
                if nums[i] < n:
                    return i
            return -1

        def addIndex(j):
            insert_index = -1
            for index, i in enumerate(sort_indexs):
                if dp[i] > dp[j]:
                    continue
                elif dp[i] < dp[j]:
                    insert_index = index
                    break
                else:  # dp 值相同，比较数值
                    if nums[j] > nums[i]:
                        continue
                    else:
                        insert_index = index
                        break
            if insert_index >= 0:
                sort_indexs.insert(insert_index, j)
            else:
                sort_indexs.append(j)

        for j in range(1, len(nums)):
            # 查找
            i = findMax(nums[j])
            if i >= 0:
                dp[j] = dp[i] + 1
            else:
                dp[j] = 1
            addIndex(j)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        '''贪心算法'''
        if not nums:
            return 0

        min_nums = [-105, nums[0]] # 长度为i的最长子序列，最小值为min_num[i]
        for i in range(1, len(nums)):
            for j in range(len(min_nums)-1):
                if nums[i] > min_nums[j]:
                    min_nums[j+1] = min(nums[i], min_nums[j+1])
            if min_nums[len(min_nums)-1] < nums[i]:
                min_nums.append(nums[i])
        return len(min_nums) - 1


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # 输出：4
    # 解释：最长递增子序列是[2, 3, 7, 101]，因此长度为 4 。

    # nums = [0, 1, 0, 3, 2, 3]
    # # 输出：4

    # nums = [7, 7, 7, 7, 7, 7, 7]
    # # 输出：1

    nums = [1, 2, -10, -8, -7]
    # 3

    solution = Solution()
    result = solution.lengthOfLIS(nums)
    print(result)