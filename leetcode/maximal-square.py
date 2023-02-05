
from typing import List


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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return 1


givenMatrix =  [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
expectedOutput = 4
result = Solution().bruteForce(givenMatrix)
print(result)
print(result == expectedOutput)