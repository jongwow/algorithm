
from typing import List

def printMatrix(mat):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            print(mat[y][x], end = ' ')
        print()

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        return 1
    def isCross(self, mat, y, x, n):
        for innerY in range(y-n+1, y+n):
            if mat[innerY][x] == 0:
                return False
        for innerX in range(x - n + 1, x + n):
            if mat[y][innerX] == 0:
                return False
        return True
    def getCross(self, mat, y, x, n):
        result=[]
        print('-'*10,y,x,n)
        for innerY in range(y-n+1, y+n):
            result.append((innerY, x))
            print(innerY, x)
            if mat[innerY][x] == 0:
                continue
                # return False
        for innerX in range(x - n + 1, x + n):
            print(y, innerX)
            result.append((y, innerX))
            if mat[y][innerX] == 0:
                continue
                # return False
        return result
        # return True
    def bruteForce(self, n, mines):
        matrix = [[1 for j in range(n)] for i in range(n)]
        for mine in mines:
            y, x = mine
            matrix[y][x] = 0

        nLen = int((n+1)/2)
        # printMatrix(matrix)

        maxInnerN = 0
        for innerN in range(1, nLen+1):
            flag = False
            for y in range(innerN - 1, n - innerN + 1):
                for x in range(innerN - 1, n - innerN + 1):
                    isCross = self.isCross(matrix, y=y, x=x,n=innerN)
                    if isCross and maxInnerN <= innerN:
                        maxInnerN = innerN
                        flag = True
                        break
                if flag:
                    break
        return maxInnerN


output = Solution().bruteForce(5, [[4, 2]])
expectedOutput = 2
print(output)