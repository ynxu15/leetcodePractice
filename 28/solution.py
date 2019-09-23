class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':                         # needle == ''
            return 0
        elif haystack == '':                     # haystack == '' and needle != ''
            return -1
        hLen, nLen = len(haystack), len(needle)
        if hLen<nLen:
            return -1
        for i in range(hLen-nLen):
            indexh, indexn = i, 0
            while indexn < nLen and indexh< hLen:
                if needle[indexn] == haystack[indexh]:
                    indexn += 1
                    indexh += 1
                else:
                    break
            if indexn == nLen and indexh <= hLen:
                return i
        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr('123', '231'))