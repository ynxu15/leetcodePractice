from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        if len(p) > len(s):
            return []
        ans = []
        p_len = len(p)
        p_map = {}
        for c in p:
            if c not in p_map:
                p_map[c] = 1
            else:
                p_map[c] += 1

        queue = []
        for index, c in enumerate(s):
            if c in p_map:
                p_map[c] -= 1
                if p_map[c] == 0:
                    del p_map[c]
            else:
                p_map[c] = -1
            queue.append(c)
            if len(queue) == p_len:
                if len(p_map) == 0:
                    ans.append(index - p_len + 1)
                c1 = queue.pop(0)

                if c1 in p_map:
                    p_map[c1] += 1
                    if p_map[c1] == 0:
                        del p_map[c1]
                else:
                    p_map[c1] = 1
        return ans



if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"

    # s = "abab"
    # p = "ab"

    solution = Solution()
    result = solution.findAnagrams(s, p)
    print(result)