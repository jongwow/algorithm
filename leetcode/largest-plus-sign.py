
from typing import List

def printMatrix(mat):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            print(mat[y][x], end = ' ')
        print()

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        matrix = [[1 for j in range(n)] for i in range(n)]
        for mine in mines:
            y, x = mine
            matrix[y][x] = 0
        dp = [[(0,0) for j in range(n)] for i in range(n)]
        reverseDP = [[(0,0) for j in range(n)] for i in range(n)]
        resultValue = 0
    
        for y in range(n):
            for x in range(n):
                if matrix[y][x] == 1:
                    left = self.getValue(n, dp,matrix, y, x-1, 0)
                    up = self.getValue(n, dp, matrix,y-1, x, 1)
                    dp[y][x] = (left + 1, up + 1)
                else:
                    dp[y][x] = (0, 0)

            
        for y in range(n-1, -1, -1):
            for x in range(n-1, -1, -1):
                if matrix[y][x] == 1:
                    right = self.getValue(n, reverseDP,matrix, y, x+1, 0)
                    down = self.getValue(n, reverseDP, matrix,y+1, x, 1)
                    reverseDP[y][x] = (right + 1, down+1)
                else:
                    reverseDP[y][x] = (0, 0)

        for y in range(n):
            for x in range(n):
                (y1, x1) = dp[y][x]
                (y2, x2) = reverseDP[y][x]
                minValue = min(y1,y2,x1,x2)
                if resultValue <= minValue:
                    resultValue = minValue
        return resultValue
    def getValue(self, n, dp, mat, y, x, dpIndex):
        if 0 <= y and y < n and 0<= x and x < n:
            if mat[y][x] == 1:
                if dp[y][x][dpIndex] != 0:
                    return dp[y][x][dpIndex]
                else:
                    return 0
            else:
                return 0
        return 0

# output = Solution().orderOfLargestPlusSign(5, [[4, 4]])
output = Solution().orderOfLargestPlusSign(5, [[4, 2]])
# output = Solution().orderOfLargestPlusSign(10, [[0,0],[0,1],[0,2],[0,7],[1,2],[1,3],[1,9],[2,3],[2,5],[2,7],[2,8],[3,2],[3,5],[3,7],[4,2],[4,3],[4,5],[4,7],[5,1],[5,4],[5,8],[5,9],[7,2],[7,5],[7,7],[7,8],[8,5],[8,8],[9,0],[9,1],[9,2],[9,8]])

# output = Solution().orderOfLargestPlusSign(5, [
#     [0, 0],[0,1],[0,3],[0,4],
#     [1,0],[1,1],[1,3],[1,4],
#     [3,0],[3,1],[3,3],[3,4],
#     [4,0],[4,1],[4,3],[4,4],

#     ])
# output = Solution().orderOfLargestPlusSign(1, [[0, 0]])
# output = Solution().orderOfLargestPlusSign(2, [[0,0],[0,1],[1,0]])
# output = Solution().orderOfLargestPlusSign(3, [[0,0]])
print(output)