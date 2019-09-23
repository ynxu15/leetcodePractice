class Solution:
    def spiralOrder(self, matrix):
        try:
            m, n = len(matrix), len(matrix[0])
            circleIndex = 0
            visitList = []
            while circleIndex < m-circleIndex and circleIndex<n-circleIndex:
                print(circleIndex, m-circleIndex, n-circleIndex)
                i,j = circleIndex, circleIndex
                for j in range(i,n-circleIndex):
                    visitList.append(matrix[i][j])
                for i in range(circleIndex+1, m-circleIndex):
                    visitList.append(matrix[i][j])
                if (m-circleIndex) - (circleIndex+1) > 0:
                    for j in range(n-circleIndex-2, circleIndex-1, -1):
                        visitList.append(matrix[i][j])
                if (n-circleIndex-2) -(circleIndex-1)>0:
                    for i in range(m-circleIndex-2,circleIndex, -1):
                        visitList.append(matrix[i][j])
                circleIndex += 1
            return visitList
        except:
            return matrix

if __name__ == '__main__':
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))