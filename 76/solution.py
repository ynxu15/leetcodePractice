from typing import Optional, List

class Solution:
    def minWindow2(self, s: str, t: str) -> str:
        map = {}
        for c in t:
            if c not in map:
                map[c] = [0, 0] # 【需要的，不需要的】
            map[c][0] += 1

        map1 = {}
        min_count = 100000000
        min_indexs = [-1, -1]
        for index, c in enumerate(s):
            if c not in map:
                continue
            if c not in map1:
                map1[c] = [index]
            else:
                map1[c].append(index)
                if len(map1[c]) > map[c][0]:
                    map1[c].pop(0)
                    map[c][1] -= 1

            # 检测是否满足要求了
            map[c][1] += 1
            if map[c][1] == map[c][0]:
                find_flag = True
                for c in map:
                    if map[c][1] < map[c][0]:
                        find_flag = False
                        break
                min_index = 1000000
                if find_flag:
                    for c in map:
                        if map1[c][0] < min_index:
                            min_index = map1[c][0]
                    if min_count > index-min_index+1:
                        min_indexs = [min_index, index]
                        min_count = index-min_index+1

            elif map[c][1] > map[c][0]: # 数量不满足
                continue

        return s[min_indexs[0]:min_indexs[1]+1]


    def minWindow(self, s: str, t: str) -> str:
        map = {}
        for c in t:
            if c not in map:
                map[c] = [0, 0] # 【需要的，不需要的】
            map[c][0] += 1

        index_queue = []
        min_count = 100000000
        min_str = ''
        for index, c in enumerate(s):
            if c not in map:
                continue

            index_queue.append(index)
            map[c][1] += 1
            if map[c][1] > map[c][0]:
                while True:
                    index = index_queue[0]
                    c1 = s[index]
                    if map[c1][1] > map[c1][0]:
                        index_queue.pop(0)
                        map[c1][1] -= 1
                    else:
                        break

            find_flag = True
            for c in map:
                if map[c][1] < map[c][0]:
                    find_flag = False
                    break
            if find_flag and index_queue[-1] - index_queue[0] + 1 < min_count:
                    min_count = index_queue[-1] - index_queue[0] + 1
                    min_str = s[index_queue[0]: index_queue[-1]+1]

        return min_str



if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    # 输出："BANC"

    # s = "a"
    # t = "a"
    # # 输出："a"

    # s = "a"
    # t = "aa"
    # # 输出: ""

    s = "acbbaca"
    t = "aba"
    #"baca"

    print(Solution().minWindow(s, t))