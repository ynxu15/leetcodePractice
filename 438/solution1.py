from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        if len(p) > len(s):
            return []
        ans = []
        p_count = [0] * 26
        diff_count = 0
        p_len = len(p)
        for c in p:
            index = ord(c)-97
            p_count[index] += 1
            if p_count[index] == 1:
                diff_count += 1

        queue = []
        for index, c in enumerate(s):
            c_index = ord(c)-97
            p_count[c_index] -= 1
            if p_count[c_index] == 0:
                diff_count -= 1
            elif p_count[c_index] == -1:
                diff_count += 1

            queue.append(c)
            if len(queue) == p_len:
                if diff_count == 0:
                    ans.append(index - p_len + 1)
                c1 = queue.pop(0)

                c1_index = ord(c1) - 97
                p_count[c1_index] += 1
                if p_count[c1_index] == 0:
                    diff_count -= 1
                elif p_count[c1_index] == 1:
                    diff_count += 1
        return ans



if __name__ == '__main__':
    # s = "cbaebabacd"
    # p = "abc"

    s = "abab"
    p = "ab"

    solution = Solution()
    result = solution.findAnagrams(s, p)
    print(result)