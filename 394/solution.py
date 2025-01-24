from typing import List

'''
先合并字符串和数字，然后再处理替换规则
'''
class Solution:

    @staticmethod
    def is_char(c):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return True

    def char_type(self, c):
        if c == '[':
            return 0
        if c == ']':
            return 1
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return 2

        if c in self.digit_set:
            return 3
        return 4


    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        char_stack = []

        self.digit_set = set([str(i) for i in range(10)])

        cache, cache_type = [], -1
        for c in s:
            if c == '[':
                c_type = 0
            elif c == ']':
                c_type = 1
            elif self.is_char(c):
                c_type = 2
            else:
                # 数字
                c_type = 3

            if c_type == cache_type and c_type > 1:
                cache.append(c)
            else:
                if cache_type > -1:
                    char_stack.append((''.join(cache), cache_type))
                cache = [c]
                cache_type = c_type

        char_stack.append((''.join(cache), cache_type))

        # 转化
        results = []
        right_brace_stack = []
        while char_stack:
            s = char_stack.pop()
            if s[0] == ']':  # 右侧括号，直接跳过
                right_brace_stack.append(s)
                continue
            if s[1] == 2:  # 字符串
                if len(char_stack) == 0:  # 这是最后一个字符串，直接出栈
                    results.insert(0, s[0])
                elif char_stack[-1][0] == '[':  # 前面是'['，取出来数字，进行重复
                    char_stack.pop()
                    sr = right_brace_stack.pop()
                    str_tmp = [s[0]]
                    while sr[0] != ']':
                        str_tmp.append(sr[0])
                        sr = right_brace_stack.pop()
                    s_digit = char_stack.pop()
                    d = int(s_digit[0])
                    gen_s = ''.join(str_tmp*d)
                    char_stack.append((gen_s, 2))
                elif char_stack[-1][1] == 2:  # 前一个如果是字符串，则两个字符串合并
                    s1 = char_stack.pop()
                    char_stack.append((s1[0]+s[0], 2))
                else:   # 前面是 ] 则需要判断 还有没有右边括号没处理
                    if len(right_brace_stack) == 0:
                        results.insert(0, s[0])
                    else:
                        right_brace_stack.append((s[0], 2))
            else:
                raise Exception("not a valid string")

        return "".join(results)

if __name__ == '__main__':
    # s = "3[a]2[bc]"
    # #输出："aaabcbc"

    # s = "3[a2[c]]"
    # #输出："accaccacc"

    # s = "2[abc]3[cd]ef"
    # #输出："abcabccdcdcdef"

    # s = "abc3[cd]xyz"
    # #输出："abccdcdcdxyz"

    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    #""zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

    solution = Solution()
    result = solution.decodeString(s)
    print(result)