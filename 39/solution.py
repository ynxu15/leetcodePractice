from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        sum_queue = [0]
        candidates_queue = [[]]
        while sum_queue:
            len_queue = len(sum_queue)
            for i in range(len_queue):
                s = sum_queue.pop(0)
                c = candidates_queue.pop(0)
                for n in candidates:
                    if c and c[-1] > n:
                        continue
                    s1 = s+n
                    if s1 == target:
                        result.append(c[:]+[n])
                    elif s1 < target:
                        candidates_queue.append(c[:]+[n])
                        sum_queue.append(s1)
                    else:
                        continue
        return result

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    #输出：[[2, 2, 3], [7]]

    # candidates = [2, 3, 5]
    # target = 8
    # #输出: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # candidates = [2]
    # target = 1
    # #输出: []

    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)