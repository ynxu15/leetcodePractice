from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 暴力解法是获得所有的子串，判断是否是回文
        # 非暴力解法
        # 包含，或者不包含当前字符

        def is_huiwen(s):
            return s == s[::-1]

        if len(s) == 1:
            return [[s]]
        cache_map = {}

        result = []
        sub_strs = []
        splits = [[s[0]]]  # 加入这个stack
        result_flag = [True] # 前面的n-1个都是回文串
        for i in range(1, len(s)):
            split_tmp, result_flag_tmp = [], []
            for j in range(len(splits)):
                r = splits[j]
                split_tmp.append(r+[s[i]])
                # 检测前n-1个
                if result_flag[j] and is_huiwen(r[-1]):
                    result_flag_tmp.append(True)
                else:
                    result_flag_tmp.append(False)
            for j in range(len(splits)):
                r = splits[j]
                split_tmp.append(r[:-1]+[r[-1]+s[i]])
                result_flag_tmp.append(result_flag[j])
            splits, result_flag = split_tmp, result_flag_tmp

        final_results = []
        for j in range(len(splits)):
            r = splits[j]
            if result_flag[j] and is_huiwen(r[-1]):
                final_results.append(r)

        return final_results


        # 子串切分行为
        # s[0] 要么是单独的，要么是和后续的字符串拼接成子串的
        # [[s0]]
        # [[s0, s1], [s0s1]]
        # [[s0, s1, s2], [s0s1, s2], [s0, s1s2], [s0s1s2]]


if __name__ == '__main__':
    s = "aab"
    #输出：[["a", "a", "b"], ["aa", "b"]]

    # s = "a"
    # #输出：[["a"]]

    s = "cdd"

    solution = Solution()
    result = solution.partition(s)
    print(result)

