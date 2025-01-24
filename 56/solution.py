from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        if len(intervals) == 1:
            return intervals
        # 1. 排序
        intervals = sorted(intervals, key=lambda x: x[0])

        # 2. 合并
        result = []
        curr = intervals[0][:]
        for interval in intervals[1:]:
            if curr[1] >= interval[0]: # 区间重合
                curr[1] = max(curr[1], interval[1])
            else: # 区间不重合
                result.append(curr)
                curr = interval[:]
        # 处理最后一个
        result.append(curr)
        return result

if __name__ == '__main__':
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # #[[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    # [[1,5]]

    solution = Solution()
    result = solution.merge(intervals)
    print(result)