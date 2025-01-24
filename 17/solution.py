from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        result = [""]
        for d in digits:
            tmp = []
            for c in digit_map[d]:
                tmp += [r+c for r in result]
            result = tmp
        return result



if __name__ == '__main__':
    digits = "23"
    #输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    # digits = ""
    # #输出：[]

    # digits = "2"
    # #输出：["a", "b", "c"]

    solution = Solution()
    result = solution.letterCombinations(digits)
    print(result)