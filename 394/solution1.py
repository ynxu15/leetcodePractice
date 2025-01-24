from typing import List

'''

遇到同是字符串/数字的，要合并
遇到数字和字符串，要进栈
遇到 [ 要进栈
遇到 ] 要出栈
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

        a_ord, z_ord = ord('a'), ord('z')
        zero_ord, nine_ord = ord('0'), ord('9')

        for c in s:
            char_ord = ord(c)
            if c == '[':
                char_stack.append(c)
            elif c == ']':
                # 出栈处理
                s_tmp = []
                c1 = char_stack.pop()
                while c1 != '[':
                    s_tmp.insert(0, c1)
                    c1 = char_stack.pop()
                n_tmp = []
                while len(char_stack) > 0:
                    c1 = char_stack[-1]
                    c1_ord = ord(c1)
                    if c1_ord >= zero_ord and c1_ord <= nine_ord:
                        n_tmp.insert(0, c1)
                        char_stack.pop()
                    else:
                        break
                n = int(''.join(n_tmp))
                for i in range(n):
                    for c1 in s_tmp:
                        char_stack.append(c1)

            elif char_ord >= a_ord and char_ord <= z_ord:  # 字母
                char_stack.append(c)
            else:  # 数字
                char_stack.append(c)

        return "".join(char_stack)

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