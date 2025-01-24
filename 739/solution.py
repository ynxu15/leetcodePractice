from typing import List

'''
超时
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if temperatures is None:
            return None
        if len(temperatures) == 0:
            return []
        outs = [0] * len(temperatures)
        need_pro_set = set()
        for index, t in enumerate(temperatures):
            removed_keys = set()
            for index1 in need_pro_set:
                if t > temperatures[index1]:
                    outs[index1] = index - index1
                    removed_keys.add(index1)
            need_pro_set = need_pro_set.difference(removed_keys)
            need_pro_set.add(index)
        return outs



if __name__ == '__main__':
    # temperatures = [73, 74, 75, 71, 69,  72, 76, 73]
    # # 输出: [1, 1, 4, 2, 1, 1, 0, 0]

    # temperatures = [30, 40, 50, 60]
    # # 输出: [1, 1, 1, 0]

    # temperatures = [30, 60, 90]
    # # 输出: [1, 1, 0]

    solution = Solution()
    result = solution.dailyTemperatures(temperatures)
    print(result)