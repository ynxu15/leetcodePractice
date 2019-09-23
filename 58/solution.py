class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(' ')
        if len(s)==0:
            return 0
        else:
            return len(s[-1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord('Hello World'))