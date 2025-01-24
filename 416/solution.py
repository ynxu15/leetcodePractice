from typing import List
class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        '''超时'''
        if not nums or len(nums) == 1:
            return False
        # 计算和，和为奇数不能分
        nums_sum = sum(nums)
        if nums_sum & 1 > 0:
            return False

        nums_len = len(nums)
        def part(index, left_sum, right_sum):
            if index == nums_len:
                if left_sum == right_sum:
                    return True
                else:
                    return False
            result = part(index+1,left_sum+nums[index], right_sum)
            if result:
                return True
            result = part(index+1, left_sum, right_sum+nums[index])
            return result

        return part(0, 0, 0)

    def canPartition2(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False
        # 计算和，和为奇数不能分
        nums_sum = sum(nums)
        if nums_sum & 1 > 0:
            return False

        nums_len = len(nums)
        target_sum = nums_sum >> 1

        try_cache = {}
        def select(index, curr_sum):
            if index == nums_len:
                if curr_sum == target_sum:
                    return True
                else:
                    return False
            if (curr_sum, nums[index]) in try_cache:
                return try_cache[(curr_sum, nums[index])]
            result = select(index+1, curr_sum+nums[index])
            if index + 1 < nums_len:
                try_cache[(curr_sum+nums[index], nums[index+1])] = result
            if result:
                return True
            result = select(index+1, curr_sum)
            try_cache[(curr_sum, nums[index])] = result
            return result

        return select(0, 0)

    def canPartition3(self, nums: List[int]) -> bool:
        '''dp解法'''
        if not nums or len(nums) == 1:
            return False
        # 计算和，和为奇数不能分
        nums_sum = sum(nums)
        if nums_sum & 1 > 0:
            return False

        nums_len = len(nums)
        target_sum = nums_sum >> 1

        dp = [[False]*(target_sum+1) for _ in range(nums_len)]
        for i in range(nums_len):
            dp[i][0] = True
        if nums[0] <= target_sum:
            dp[0][nums[0]] = True
        for i in range(1, nums_len):
            for j in range(1, target_sum+1):
                if j > nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    def canPartition(self, nums: List[int]) -> bool:
        '''使用位图和dp结合'''
        s = sum(nums)
        if s & 1: return False
        t = 1 << (s >> 1)
        # s >> 1 是处以2，是目标值 target
        # 1<<target 是用target长度位数的位图，位图里1表示可以达到的数True，0表示不可达到的数
        # t 最低位0位置表示target这个值是否可以达到
        # target+1位置表示求和0的值是否可以达到，那如果所有数都不选的话，那就是target+1位图设置为1
        for x in nums:
            t |= t >> x
            # 每次处理一个数，将位图上表示的数加上x,就得到了选用x后，新的可达的数；如果不选择x,那原来可达的数，还是可以用t表示
            # 那两次可达的数，就是求或
        return bool(t & 1)


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    # 输出：true
    # 解释：数组可以分割成[1, 5, 5] 和[11] 。

    # nums = [1, 2, 3, 5]
    # # 输出：false
    # # 解释：数组不能分割成两个元素和相等的子集。

    # nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
    #  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]

    nums = [1, 1]

    solution = Solution()
    result = solution.canPartition(nums)
    print(result)