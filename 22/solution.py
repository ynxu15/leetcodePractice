from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        result = []
        def genHelp(l_count, r_count):
            if l_count == n and r_count == n:
                result.append("".join(stack))
                return
            if l_count > r_count:
                if l_count >= n:  # 只能右括号入栈
                    stack.append(")")
                    genHelp(l_count, r_count+1)
                    stack.pop()
                else:  # 两个都可以入栈
                    stack.append("(")
                    genHelp(l_count + 1, r_count)
                    stack.pop()
                    stack.append(")")
                    genHelp(l_count, r_count+1)
                    stack.pop()
            else:  # 只能选择左括号入栈
                stack.append("(")
                genHelp(l_count+1, r_count)
                stack.pop()

        genHelp(0, 0)
        return result

if __name__ == '__main__':
    n = 3
    #输出：["((()))", "(()())", "(())()", "()(())", "()()()"]

    # n = 1
    # #输出：["()"]

    solution = Solution()
    result = solution.generateParenthesis(n)
    print(result)