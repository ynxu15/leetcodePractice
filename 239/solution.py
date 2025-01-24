from typing import Optional, List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''递减序列'''
        import collections
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res

if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    #输出：[3, 3, 5, 5, 6, 7]

    # nums = [1]
    # k = 1
    # #输出：[1]

    # nums = [1, -1]
    # k = 1
    # # [1, -1]

    nums = [1, 3, 1, 2, 0, 5]
    k = 3
    #[3, 3, 2, 5]

    print(Solution().maxSlidingWindow(nums, k))