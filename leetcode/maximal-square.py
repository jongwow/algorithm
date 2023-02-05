
from typing import List

def printMatrix(mat):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            print(mat[y][x], end = ' ')
        print()

class Solution:
    def bruteForce(self, matrix: List[List[str]]) -> int:
        largestSquare = 0
        possiblePositions = []
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                # select upperTop
                if matrix[y][x] == '0':
                    continue
                for rY in range(y, len(matrix)):
                    yDiff = rY - y
                    if x + yDiff >= len(matrix[rY]):
                        break
                    possiblePositions.append((y, x, rY, x + yDiff))
        for y, x, rY, rX in possiblePositions:
            flag = True
            cnt = 0
            for innerY in range(y, rY + 1):
                for innerX in range(x, rX + 1):
                    if matrix[innerY][innerX] == '0':
                        flag = False
                        break
                    cnt+=1
                if not flag:
                    break
            if flag and largestSquare < cnt:
                largestSquare = cnt
        return largestSquare
    def isSafe(self, pos):
        y, x = pos
        if x < 0 or x >= self.xLen or y < 0 or y >= self.yLen:
            return False
        return True
    def getValue(self, pos, mat, dp):
        if self.isSafe(pos):
            y,x= pos
            if mat[y][x] == '1':
                if dp[y][x] != 0:
                    return dp[y][x]
                else:
                    return 1
            else:
                return 0
        else:
            return 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.yLen = len(matrix)
        self.xLen = len(matrix[0])
        dp = [[0 for j in range(self.xLen)] for i in range(self.yLen)]
        for y in range(self.yLen):
            for x in range(self.xLen):
                if matrix[y][x] == '0':
                    continue
                leftX = x-1
                upY = y-1
                left = (y, leftX)
                leftUp = (upY, leftX)
                up = (upY, x)
                leftValue = self.getValue(left, matrix, dp)
                leftUpValue = self.getValue(leftUp, matrix, dp)
                upValue = self.getValue(up, matrix, dp)
                minValue = min(leftValue, leftUpValue, upValue)
                minValue += 1
                if dp[y][x] < minValue:
                    dp[y][x] = minValue
        result = 0
        for y in range(self.yLen):
            for x in range(self.xLen):
                if result <= dp[y][x]:
                    result = dp[y][x]
        return result**2


givenMatrix1 =  [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
givenMatrix2 =  [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
expectedOutput = 4
result = Solution().maximalSquare(givenMatrix2)
result2 = Solution().bruteForce(givenMatrix2)
print(result2)
# result = Solution().bruteForce(givenMatrix)
print(result)
# print(result == expectedOutput)