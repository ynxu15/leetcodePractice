from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 不排序做法
        left_right_map = {}  # (l, r)
        seq_max_len = 0
        for n in nums:
            if n in left_right_map:
                continue
            # 还不存在这个数
            l, r = n, n
            if n-1 in left_right_map:  # 左边接上了
                l1, r1= left_right_map[n-1]
                l = l1
                left_right_map[n-1] = [l1, r1]
            if n + 1 in left_right_map:  # 右边接上了
                l2, r2 = left_right_map[n + 1]
                r = r2
                left_right_map[n + 1] = [l2, r2]

            # 修改边界的两个节点的情况
            left_right_map[n] = [l, r]
            left_right_map[l][1] = r
            left_right_map[r][0] = l

        # 遍历所有数，找出边界节点
        for n in left_right_map:
            l, r = left_right_map[n]
            if l != n and r != n:
                continue
            else:
                num = r - l + 1
                if num > seq_max_len:
                    seq_max_len = num
        return seq_max_len



if __name__ == '__main__':
    #nums =  [100,4,200,1,3,2] #4
    #nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] #9
    #nums = [1,2,0,1]  #3
    nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7] # 4

    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)