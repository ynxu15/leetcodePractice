from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        st = set(nums)  # 把 nums 转成哈希集合
        for x in st:
            if x - 1 in st:
                continue
            # x 是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
        return ans

