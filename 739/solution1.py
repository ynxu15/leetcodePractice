from typing import List

'''
维护一个目前还没找到的栈，栈底到栈顶是从大到小，那对应的index肯定是从大到小排序
每次增加一个值，仅需要逐次栈顶对比大小即可
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if temperatures is None:
            return None
        if len(temperatures) == 0:
            return []
        outs = [0] * len(temperatures)
        need_pro_stack = []
        for index, t in enumerate(temperatures):
            removed_keys = set()
            while len(need_pro_stack) > 0 and need_pro_stack[-1][0] < t:
                t1, index1 = need_pro_stack.pop()
                outs[index1] = index-index1
            need_pro_stack.append((t, index))
        return outs



if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69,  72, 76, 73]
    # 输出: [1, 1, 4, 2, 1, 1, 0, 0]

    # temperatures = [30, 40, 50, 60]
    # # 输出: [1, 1, 1, 0]

    # temperatures = [30, 60, 90]
    # # 输出: [1, 1, 0]

    solution = Solution()
    result = solution.dailyTemperatures(temperatures)
    print(result)