import copy
class Solution:
    def solveNQueens(self, n):
        row = list(range(n))
        column = [-100]*n
        dValues = [-100]*n
        dValuesSum = [-1]*n
        results = []
        def tryIndex(index):
            #print('index', index)
            if index == n:
                #print('index, n', index, n)
                results.append(copy.copy(column))
                return
            for p in range(n):
                #print('p', index, p, n)
                if p in column:
                    continue
                continueFlag = False
                for i in range(0, index):
                    if abs(index-i) == abs(p - column[i]):
                        continueFlag = True
                        break
                if continueFlag:
                    continue
                # if index-p in dValues or index+p in dValues:
                #     continue
                column[index] = p
                dValues[index] = index-p
                dValuesSum[index] = index + p
                tryIndex(index+1)
                column[index] = -1
                dValues[index] = -100
                dValuesSum[index] = -100
        tryIndex(0)
        for result in results:
            print(result)
        resultStr = []
        for r in results:
            rStrTmp, column = [], r
            for i in range(n):
                strTmp = ''
                for j in range(n):
                    if j == column[i]:
                        strTmp += 'Q'
                    else:
                        strTmp += '.'
                rStrTmp.append(strTmp)
            resultStr.append(rStrTmp)
        print(resultStr)
        return resultStr

if __name__ == '__main__':
    Solution().solveNQueens(4)