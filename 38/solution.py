class Solution:
    def countAndSay(self, n: int) -> str:
        if n <=1:
            return '1'
        s = '1'
        for i in range(1, n):
            s = self.getNextString(s)
        return s

    def getNextString(self, s):
        chTmp, num, sNew = 'a', 0, ''
        #print('s', s)
        for c in s:
            if c == chTmp:
                num += 1
            else:
                sNew = sNew+str(num)+chTmp
                #print('c', c, sNew)
                chTmp = c
                num = 1
        sNew = sNew  + str(num)+ chTmp
        return sNew[2:]

if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(4))

