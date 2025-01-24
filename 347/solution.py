from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return
        nums_map = {}
        for n in nums:
            if n in nums_map:
                nums_map[n] += 1
            else:
                nums_map[n] = 1

        # 排序
        result = sorted(list(nums_map.items()), key=lambda x:x[1])
        return [r[0] for r in result[-k:]]


if __name__ == '__main__':
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    # 输出: [1, 2]

    nums = [1]
    k = 1
    # # 输出: [1]

    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)