from typing import List


class Solution:
    def minimumTotalV1(self, triangle: List[List[int]]) -> int:
        dp = {}
        h = len(triangle)

        def solve(r, c):
            # base case
            id = "%d_%d" % (r, c)
            if id in dp:

                return dp[id]
            # base case 2 범위 밖
            if r < 0 or r > h:
                return 0
            if c < 0 or c > r:
                return 0
            # base case 3 종점
            if r == h-1:
                return triangle[r][c]

            dp[id] = triangle[r][c] + min(solve(r+1, c), solve(r+1, c+1))
            return dp[id]
        ans = solve(0, 0)
        return ans


sol = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(sol.minimumTotal([[-10]]))
