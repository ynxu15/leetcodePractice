from typing import List

'''
O(N)
根据数的某一位，二分
2^15
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        if k > len(nums):
            return None

        small_map, big_map = {}, {}
        small_count, big_count = 0, 0
        # 所有数加上10000
        # 2^15
        move_step = 14
        for n in nums:
            n += 10000
            if n >> move_step & 1 == 1:
                if n in big_map:
                    big_map[n] += 1
                else:
                    big_map[n] = 1
                big_count += 1
            else:
                if n in small_map:
                    small_map[n] += 1
                else:
                    small_map[n] = 1
                small_count += 1
        while move_step >= 0:
            move_step -= 1
            if big_count >= k:
                target_map = big_map
            else:
                target_map = small_map
                k -= big_count
            if len(target_map) == 1:
                return list(target_map.keys())[0]-10000

            big_map, small_map = {}, {}
            big_count, small_count = 0, 0
            for n in target_map:
                if n >> move_step & 1 == 1:
                    big_map[n] = target_map[n]
                    big_count += target_map[n]
                else:
                    small_map[n] = target_map[n]
                    small_count += target_map[n]

        return 0


if __name__ == '__main__':
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 2
    # #输出: 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    # 输出: 4

    solution = Solution()
    result = solution.findKthLargest(nums, k)
    print(result)