from typing import List

import copy

# 1438


def getMirror(c, n):
    return 2 * n - 2 - c


def printArray(n, a="Unnamed"):
    print('=======', a, '=====')
    for a in n:
        print(a)


cnt = 0


class SolutionSlow:
    def __init__(self) -> None:
        self.dp = [[]]

    def cherryPickup(self, grid: List[List[int]]) -> int:

        # n*2*n*2 로 만들어서
        n = len(grid)
        new_grid = [[0 for j in range(2*n-1)] for i in range(2*n-1)]
        self.dp = [[-1 for j in range(2*n-1)] for i in range(2*n-1)]

        # 거울세상.
        i = 0

        while i < 2 * n - 1:
            j = 0
            while j < 2 * n - 1:
                if i < n and j < n:
                    new_grid[i][j] = grid[i][j]
                elif i >= n and j >= n:
                    new_grid[i][j] = grid[getMirror(i, n)][getMirror(j, n)]
                elif i >= n and j < n:
                    new_grid[i][j] = grid[getMirror(i, n)][j]
                elif i < n and j >= n:
                    new_grid[i][j] = grid[i][getMirror(j, n)]
                else:
                    assert False
                j += 1
            i += 1

        # === PICK === #
        ans = self.cherryPickup_inner(n, 0, 0, new_grid)
        return ans
        # 하나 먹으면 거울세상의 것도 먹음

    def cherryPickup_inner_wrong(self, n: int, r: int, c: int, bigGrid: List[List[int]]) -> int:
        if self.dp[r][c] != -1:
            return self.dp[r][c]
        global cnt
        cnt += 1
        print('cherryPickup', n, r, c, cnt)
        printArray(bigGrid)
        bd = 2 * n - 1
        if r == bd - 1 and c == bd - 1:
            return bigGrid[getMirror(r, n)][getMirror(c, n)]
        opts = -1
        # left
        if r + 1 < bd and (bigGrid[getMirror(r+1, n)][getMirror(c, n)] == 0 or bigGrid[getMirror(r+1, n)][getMirror(c, n)] == 1):
            cherry = bigGrid[getMirror(r+1, n)][getMirror(c, n)]
            bigGrid[getMirror(r+1, n)][getMirror(c, n)] = bigGrid[r+1][c] = 0
            opts = max(opts, cherry +
                       self.cherryPickup_inner(n, r+1, c, bigGrid))
            bigGrid[getMirror(r+1, n)][getMirror(c, n)
                                       ] = bigGrid[r+1][c] = cherry
        # down
        if c + 1 < bd and (bigGrid[getMirror(r, n)][getMirror(c+1, n)] == 0 or bigGrid[getMirror(r, n)][getMirror(c+1, n)] == 1):
            cherry = bigGrid[getMirror(r, n)][getMirror(c+1, n)]
            bigGrid[getMirror(r, n)][getMirror(c+1, n)] = bigGrid[r][c+1] = 0
            opts = max(opts, cherry +
                       self.cherryPickup_inner(n, r, c+1, bigGrid))
            bigGrid[getMirror(r, n)][getMirror(
                c+1, n)] = bigGrid[r][c+1] = cherry
        self.dp[r][c] = opts
        return opts

    def cherryPickup_inner(self, n: int, r: int, c: int, bigGrid: List[List[int]]) -> int:
        bd = 2 * n - 1
        if r == bd - 1 and c == bd - 1:
            return bigGrid[getMirror(r, n)][getMirror(c, n)]
        opts = -1
        # left
        if r + 1 < bd and (bigGrid[getMirror(r+1, n)][getMirror(c, n)] == 0 or bigGrid[getMirror(r+1, n)][getMirror(c, n)] == 1):
            cherry = bigGrid[getMirror(r+1, n)][getMirror(c, n)]
            bigGrid[getMirror(r+1, n)][getMirror(c, n)] = bigGrid[r+1][c] = 0
            opts = max(opts, cherry +
                       self.cherryPickup_inner(n, r+1, c, bigGrid))
            bigGrid[getMirror(r+1, n)][getMirror(c, n)
                                       ] = bigGrid[r+1][c] = cherry
        # down
        if c + 1 < bd and (bigGrid[getMirror(r, n)][getMirror(c+1, n)] == 0 or bigGrid[getMirror(r, n)][getMirror(c+1, n)] == 1):
            cherry = bigGrid[getMirror(r, n)][getMirror(c+1, n)]
            bigGrid[getMirror(r, n)][getMirror(c+1, n)] = bigGrid[r][c+1] = 0
            opts = max(opts, cherry +
                       self.cherryPickup_inner(n, r, c+1, bigGrid))
            bigGrid[getMirror(r, n)][getMirror(
                c+1, n)] = bigGrid[r][c+1] = cherry
        return opts


class SolutionWrong:
    def __init__(self) -> None:
        self.dp = [[]]

    def cherryPickup(self, grid: List[List[int]]) -> int:

        n = len(grid)
        new_grid = [[0 for j in range(2*n-1)] for i in range(2*n-1)]
        self.dp = [[-1 for j in range(2*n-1)] for i in range(2*n-1)]

        i = 0
        while i < 2 * n - 1:
            j = 0
            while j < 2 * n - 1:
                if i < n and j < n:
                    new_grid[i][j] = grid[i][j]
                elif i >= n and j >= n:
                    new_grid[i][j] = grid[getMirror(i, n)][getMirror(j, n)]
                elif i >= n and j < n:
                    new_grid[i][j] = grid[getMirror(i, n)][j]
                elif i < n and j >= n:
                    new_grid[i][j] = grid[i][getMirror(j, n)]
                else:
                    assert False
                j += 1
            i += 1
        ans = self.cherryPickup_inner(n, 0, 0, new_grid)
        return ans

    def cherryPickup_inner(self, n: int, r: int, c: int, bigGrid: List[List[int]]) -> int:
        if self.dp[r][c] != -1:
            return self.dp[r][c]
        bd = 2 * n - 1
        if r == bd - 1 and c == bd - 1:
            return bigGrid[getMirror(r, n)][getMirror(c, n)]
        opts = -1
        # left
        if r + 1 < bd and (bigGrid[getMirror(r+1, n)][getMirror(c, n)] == 0 or bigGrid[getMirror(r+1, n)][getMirror(c, n)] == 1):
            cherry = bigGrid[getMirror(r+1, n)][getMirror(c, n)]
            bigGrid[getMirror(r+1, n)][getMirror(c, n)] = bigGrid[r+1][c] = 0
            opts = max(opts, cherry +
                       self.cherryPickup_inner(n, r+1, c, bigGrid))
            bigGrid[getMirror(r+1, n)][getMirror(c, n)
                                       ] = bigGrid[r+1][c] = cherry
        # down
        if c + 1 < bd and (bigGrid[getMirror(r, n)][getMirror(c+1, n)] == 0 or bigGrid[getMirror(r, n)][getMirror(c+1, n)] == 1):
            cherry = bigGrid[getMirror(r, n)][getMirror(c+1, n)]
            bigGrid[getMirror(r, n)][getMirror(c+1, n)] = bigGrid[r][c+1] = 0
            opts = max(opts, cherry +
                       self.cherryPickup_inner(n, r, c+1, bigGrid))
            bigGrid[getMirror(r, n)][getMirror(
                c+1, n)] = bigGrid[r][c+1] = cherry
        self.dp[r][c] = opts
        return opts


class SolutionSlow2:
    def __init__(self) -> None:
        self.grid = [[]]
        self.n = 0

    def cherryPickup(self, grid: List[List[int]]) -> int:
        origin_grid = copy.deepcopy(grid)
        self.grid = grid
        self.n = len(grid)
        # Dynamic Programming
        # - 나눠서 생각해보자.
        # - 처음에 내려갈 때, 그리고 다시 올라올 때
        # - 처음에 내려갈 때에 대한 모든 경우에 대해서 결과를 저장
        # - 다시 올라갈 때는 위 경우들에서부터 시작해서 올라가기.
        # (옆으로 갈때, 아래로 갈때)
        val = grid[0][0]
        grid[0][0] = 0
        candidates = self.cherryPickupDown(0, 0, '')
        results = [(p, v+val) for (p, v) in candidates]
        grid[0][0] = val
        # TODO: 만약 시작점에 1이었다면 추가해줘야함.
        if len(results) == 0:
            return 0
        path_len = len(results[0][0])
        opt = -1
        max_path = ''
        for rc in results:
            (path, value) = rc
            # Walk
            r = 0
            c = 0
            for idx in range(path_len):
                if path[idx] == 'R':
                    self.grid[r][c] = 0
                    c += 1
                else:
                    self.grid[r][c] = 0
                    r += 1
            self.grid[r][c] = 0
            candidates = self.cherryPickupDown(0, 0, '')
            for cc in candidates:
                opt = max(opt, value + cc[1])
                max_path = path + cc[0]
            # Revert
            self.grid = copy.deepcopy(origin_grid)
        print('max path:', max_path)
        printArray(origin_grid, "After all this")
        return opt

    def cherryPickupDown(self, r: int, c: int, path: str) -> List[int]:
        if r == self.n-1 and c == self.n-1:
            return [(path, 0)]
        down_cases = []
        right_cases = []
        if c + 1 < self.n and self.grid[r][c+1] != -1:
            val = self.grid[r][c+1]
            self.grid[r][c+1] = 0
            right_path = path+'R'
            right_deep = self.cherryPickupDown(r, c+1, right_path)
            right_cases = [(p, v+val) for (p, v) in right_deep]
            self.grid[r][c+1] = val
        if r + 1 < self.n and self.grid[r+1][c] != -1:
            val = self.grid[r+1][c]
            self.grid[r+1][c] = 0
            down_path = path+'D'
            down_deep = self.cherryPickupDown(r+1, c, down_path)
            down_cases = [(p, v+val) for (p, v) in down_deep]
            self.grid[r+1][c] = val
        if len(down_cases) == 0 and len(right_cases) == 0:
            # print("BOOM")
            pass
        return right_cases + down_cases


class SolutionSlow3:
    def __init__(self) -> None:
        self.grid = [[]]
        self.n = 0

    def cherryPickup(self, grid: List[List[int]]) -> int:
        origin_grid = copy.deepcopy(grid)
        self.grid = grid
        self.n = len(grid)
        # Dynamic Programming
        # - 나눠서 생각해보자.
        # - 처음에 내려갈 때, 그리고 다시 올라올 때
        # - 처음에 내려갈 때에 대한 모든 경우에 대해서 결과를 저장
        # - 다시 올라갈 때는 위 경우들에서부터 시작해서 올라가기.
        # (옆으로 갈때, 아래로 갈때)
        val = grid[0][0]
        grid[0][0] = 0
        candidates = self.cherryPickupDown(0, 0, '')
        results = [(p, v+val) for (p, v) in candidates]
        grid[0][0] = val
        # TODO: 만약 시작점에 1이었다면 추가해줘야함.
        if len(results) == 0:
            return 0
        path_len = len(results[0][0])
        opt = -1
        max_path = ''
        for rc in results:
            (path, value) = rc
            # Walk
            r = 0
            c = 0
            for idx in range(path_len):
                if path[idx] == 'R':
                    self.grid[r][c] = 0
                    c += 1
                else:
                    self.grid[r][c] = 0
                    r += 1
            self.grid[r][c] = 0
            candidates = self.cherryPickupDown(0, 0, '')
            for cc in candidates:
                opt = max(opt, value + cc[1])
                max_path = path + cc[0]
            # Revert
            self.grid = copy.deepcopy(origin_grid)
        print('max path:', max_path)
        printArray(origin_grid, "After all this")
        return opt

    def cherryPickupDown(self, r: int, c: int, path: str) -> List[int]:
        if r == self.n-1 and c == self.n-1:
            return [(path, 0)]
        down_cases = []
        right_cases = []
        if c + 1 < self.n and self.grid[r][c+1] != -1:
            val = self.grid[r][c+1]
            self.grid[r][c+1] = 0
            right_path = path+'R'
            right_deep = self.cherryPickupDown(r, c+1, right_path)
            right_cases = [(p, v+val) for (p, v) in right_deep]
            self.grid[r][c+1] = val
        if r + 1 < self.n and self.grid[r+1][c] != -1:
            val = self.grid[r+1][c]
            self.grid[r+1][c] = 0
            down_path = path+'D'
            down_deep = self.cherryPickupDown(r+1, c, down_path)
            down_cases = [(p, v+val) for (p, v) in down_deep]
            self.grid[r+1][c] = val
        if len(down_cases) == 0 and len(right_cases) == 0:
            # print("BOOM")
            pass
        return right_cases + down_cases


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        dp = {}
        self.cherryPickupInner(n, 0, 0, 0, 0, grid, dp)
        if len(dp) == 0 or dp[(0, 0, 0, 0)] < 0:
            return 0
        return dp[(0, 0, 0, 0)]

    def cherryPickupInner(self, n: int, x1, y1, x2, y2, grid, memo):
        cherryPicked = float('-inf')
        # base case
        if x1 >= n or y1 >= n or x2 >= n or y2 >= n:
            return cherryPicked
        # cached case
        if (x1, y1, x2, y2) in memo:
            return memo[(x1, y1, x2, y2)]
        # simple case
        if grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return cherryPicked
        elif x1 == x2 and y1 == y2:
            cherryPicked = grid[x1][y1]
        else:
            cherryPicked = grid[x1][y1] + grid[x2][y2]

        if x1 == n-1 and y1 == n-1:
            return grid[x1][y1]
        if x2 == n-1 and y2 == n-1:
            return grid[x2][y2]

        # general case
        cherryPicked += max([
            self.cherryPickupInner(n, x1+1, y1, x2+1, y2, grid, memo),
            self.cherryPickupInner(n, x1, y1+1, x2, y2+1, grid, memo),
            self.cherryPickupInner(n, x1, y1+1, x2+1, y2, grid, memo),
            self.cherryPickupInner(n, x1+1, y1, x2, y2+1, grid, memo),
        ])
        memo[(x1, y1, x2, y2)] = cherryPicked
        return cherryPicked


"""
0  1 -1
1  0 -1
1  1  1
"""

tcs = [
    [[0, 1, -1], [1, 0, -1], [1, 1, 1]],
    [[1, 1, -1], [1, -1, 1], [-1, 1, 1]],
    [[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1,
                                                                           0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1]],
    [[1, 1, 1, 1, -1, -1, -1, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, -1, 1, 1], [0, 0, 0, 0, 1, -1, 0, 0, 1, -1],
        [1, 0, 1, 1, 1, 0, 0, -1, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, -1], [1, -1, 0, 1, 0, 0, 0, 1, -1, 1], [1, 0, -1, 0, -1, 0, 0, 1, 0, 0], [0, 0, -1, 0, 1, 0, 1, 0, 0, 1]]

]
"""
[1, 1, 1, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 1]
[1, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 1]
# RRRDDRRRDDDD + DDDRRRDDDRRR
DDDDDDRRRRRRDDDDDDRRRRRR
"""

for tc in tcs:
    # print(genStr(tc))
    printArray(tc)
    sol = Solution().cherryPickup(tc)
    print(sol)

# 현재 좌표 + 경로.
# -> 오직 하나만 존재.
# 그러면 이걸 어떻게 DP로 풀 수 있을까?
# Dynamic Programming
# - 나눠서 생각해보자.
# - 처음에 내려갈 때, 그리고 다시 올라올 때
# - 처음에 내려갈 때에 대한 모든 경우에 대해서 결과를 저장
# - 다시 올라갈 때는 위 경우들에서부터 시작해서 올라가기.
