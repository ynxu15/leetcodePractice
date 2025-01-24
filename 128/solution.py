from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 1. 排序
        nums1 = sorted(nums)

        # 2. 找最长数字连续序列
        seq_max_size = 0
        max_seq_tmp = 1
        for i in range(1, len(nums1)):
            if nums1[i - 1] + 1 == nums1[i]:
                max_seq_tmp += 1
            elif nums1[i - 1] == nums1[i]:
                continue
            else:
                if max_seq_tmp > seq_max_size:
                    seq_max_size = max_seq_tmp
                max_seq_tmp = 1

        if max_seq_tmp > seq_max_size:
            seq_max_size = max_seq_tmp
        return seq_max_size


if __name__ == '__main__':
    # nums =  [100,4,200,1,3,2]
    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    #nums = [1,2,0,1]
    nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]

    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)