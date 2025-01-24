from typing import Optional, List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        count = 0
        while left<right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            min_height = min(left_max, right_max)
            if left_max < right_max:
                left += 1
                if min_height > height[left]:
                    count += (min_height-height[left])
            else:
                right -= 1
                if min_height > height[right]:
                    count += (min_height-height[right])
        return count



if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    #6

    # height = [4, 2, 0, 3, 2, 5]
    # # 输出：9

    print(Solution().trap(height))