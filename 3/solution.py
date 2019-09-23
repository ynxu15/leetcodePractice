class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strList, maxLen, lenTmp = [], 0, 0
        for ch in s:
            if ch not in strList:
                lenTmp += 1
                strList.append(ch)
            else:
                print('pre', strList)
                index = strList.index(ch)
                strList = strList[index+1:]
                strList.append(ch)
                #print(strList)
                if maxLen<lenTmp:
                    maxLen = lenTmp
                lenTmp = len(strList)
        if maxLen < lenTmp:
            maxLen = lenTmp
        return maxLen

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))