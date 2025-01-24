from typing import List


class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        if not wordDict:
            return False
        wordLenDic = {}
        for word in wordDict:
            wordLenDic[word] = len(word)

        checkMap = {}
        def check(s):
            if s == "":
                return True
            if s in checkMap:
                return checkMap[s]
            s_len = len(s)
            for word in wordDict:
                word_len = wordLenDic[word]
                if s_len < word_len:
                    continue
                if s[:word_len] == word:
                    result = check(s[word_len:])
                    if result:
                        checkMap[s[word_len:]] = True
                        checkMap[s] = True
                        return True
            checkMap[s] = False
            return False
        return check(s)

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        '''动态规划'''
        if not s:
            return False
        if not wordDict:
            return False
        dp = [False] * len(s)
        wordLenDic = {}
        for word in wordDict:
            wordLenDic[word] = len(word)
        for i in range(len(s)):
            for word in wordDict:
                word_len = wordLenDic[word]
                if word_len > i+1:
                    continue
                if s[i+1-word_len:i+1] == word:
                    if i-word_len < 0:
                        dp[i] = True
                        break
                    else:
                        if dp[i-word_len]:
                            dp[i] = True
                            break
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''动态规划'''
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    # s = "leet"
    # wordDict = ["leet", "code"]

    s = "leetcode"
    wordDict = ["leet", "code"]
    # 输出: true

    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    # # 输出: true


    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # # 输出: false

    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    # wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

    solution = Solution()
    result = solution.wordBreak(s, wordDict)
    print(result)