# Graph General
from typing import List

# BFS나 DFS로 풀면 될 것 같다.


class Solution:
    def __init__(self) -> None:
        self.data = [[]]
        self.visited = [[]]
        self.len_row = 0
        self.len_col = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        return self.numIslandsDFS(grid)

    def visit(self, r, c):
        self.visited[r][c] = True
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + d[0], c + d[1]
            if nr < 0 or nr >= self.len_row or nc < 0 or nc >= self.len_col:
                continue
            if self.data[nr][nc] == "1" and self.visited[nr][nc] == False:
                self.visit(nr, nc)

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        self.data = grid
        self.visited = [[False for i in grid[0]] for j in grid]
        self.len_row = len(grid)
        self.len_col = len(grid[0])
        cnt = 0
        for r in range(self.len_row):
            for c in range(self.len_col):
                if self.data[r][c] == "1" and self.visited[r][c] == False:
                    cnt += 1
                    self.visit(r, c)
        return cnt

    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        cnt = 0
        len_y = len(grid)
        len_x = len(grid[0])
        idx_x, idx_y = 0, 0
        while idx_y < len_y:
            idx_x = 0
            while idx_x < len_x:
                if grid[idx_y][idx_x] == "1":
                    cnt += 1
                    grid[idx_y][idx_x] = "0"
                    queue = [(idx_y, idx_x)]
                    while len(queue) != 0:
                        current = queue.pop()  # BFS
                        # print(cnt, current)
                        # 상: idx_y - 1, idx_x
                        # 하: idx_y + 1, idx_x
                        # 좌: idx_y, idx_x - 1
                        # 우: idx_y, idx_x + 1
                        if 0 <= current[0] - 1 and current[0] - 1 < len_y and 0 <= current[1] and current[1] < len_x and grid[current[0]-1][current[1]] == "1":
                            grid[current[0]-1][current[1]] = "0"
                            queue.append((current[0] - 1, current[1]))
                        if 0 <= current[0] + 1 and current[0] + 1 < len_y and 0 <= current[1] and current[1] < len_x and grid[current[0]+1][current[1]] == "1":
                            grid[current[0]+1][current[1]] = "0"
                            queue.append((current[0] + 1, current[1]))
                        if 0 <= current[0] and current[0] < len_y and 0 <= current[1] - 1 and current[1] - 1 < len_x and grid[current[0]][current[1] - 1] == "1":
                            grid[current[0]][current[1]-1] = "0"
                            queue.append((current[0], current[1] - 1))
                        if 0 <= current[0] and current[0] < len_y and 0 <= current[1] + 1 and current[1] + 1 < len_x and grid[current[0]][current[1] + 1] == "1":
                            grid[current[0]][current[1]+1] = "0"
                            queue.append((current[0], current[1] + 1))
                idx_x += 1
            idx_y += 1
        # print(grid)
        return cnt


tcs = [
    # [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ],  # 1
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]  # 3
]
for tc in tcs:
    sol = Solution().numIslands(tc)
    print(sol)
