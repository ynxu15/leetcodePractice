from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return [0]

        char_set = [-1]*26  # 集合的指针，同一个集合的构成一个树
        char_count = [0]*26  # 每个字母出现的次数
        head_queue = []
        a_ord = ord('a')
        for c in s:
            c_index = ord(c)-a_ord
            char_count[c_index] += 1
            if char_set[c_index] == -1:  # 它是头
                char_set[c_index] = c_index
                head_queue.append(c_index)
            else:
                for i in range(len(head_queue)-1, -1, -1):
                    if head_queue[i] == c_index:
                        break
                    else:
                        c1_index =head_queue[i]
                        if char_set[c1_index] == c1_index:
                            char_set[c1_index] = char_set[c_index]

                # if len(head_char_set) == 1 and c_index in head_char_set:
                #     continue
                # for c1_index in head_char_set:
                #     char_set[c1_index] = char_set[c_index]
                # head_char_set = set()
        set_queue = []
        chars = set()
        for c in s:
            c_index = ord(c)-a_ord
            if c_index in chars:
                continue
            chars.add(c_index)
            if char_set[c_index] == c_index:
                set_queue.append(c_index)
            elif char_set[c_index] == -1:
                continue
            else:
                if char_count[c_index] == -1:  # 说明这个已经处理过了
                    continue
                pre_index = c_index
                while char_set[pre_index] != pre_index:  # 往上找集合的头
                    pre_index = char_set[pre_index]
                char_count[pre_index] += char_count[c_index]  # 计数
                char_count[c_index] = -1

        ans = [char_count[c_index] for c_index in set_queue]
        return ans


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    # 输出：[9, 7, 8]

    s = "eccbbbbdec"
    # 输出：[10]

    s = "caedbdedda"
    #[1, 9]

    solution = Solution()
    result = solution.partitionLabels(s)
    print(result)