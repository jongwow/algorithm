from typing import List


class Solution:
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        r = (0, 1)
        d = (1, 0)
        l = (0, -1)
        u = (-1, 0)
        dirs = [r, d, l, u]
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        lng = m * n
        path = []
        # l 반복
        # 만약 벽 / 이미 지나간 곳
        # -> 방향 전환
        # -> 만약 벽 / 이미 지나간 곳 -> return
        current_row = 0
        current_col = 0
        dirs_idx = 0
        while len(path) < lng:
            print(current_row, current_col)
            path.append(matrix[current_row][current_col])
            visited[current_row][current_col] = 1
            dir = dirs[dirs_idx]
            next_row, next_col = current_row+dir[0], current_col+dir[1]
            # 더이사 진행이 불가능하다면
            if next_row < 0 or next_row > m - 1 or next_col < 0 or next_col > n - 1 or visited[next_row][next_col] == 1:
                print('direct: ', dirs_idx, end='->')
                dirs_idx = 0 if (dirs_idx + 1) % 4 == 0 else dirs_idx + 1
                print(dirs_idx)
            current_row, current_col = next_row, next_col
        return path

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = (0, 1)
        d = (1, 0)
        l = (0, -1)
        u = (-1, 0)
        dirs = [r, d, l, u]
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        lng = m * n
        path = []
        # l 반복
        # 만약 벽 / 이미 지나간 곳
        # -> 방향 전환
        # -> 만약 벽 / 이미 지나간 곳 -> return
        current_row = 0
        current_col = 0
        dirs_idx = 0
        visited[current_row][current_col] = 1
        path.append(matrix[current_row][current_col])
        while len(path) < lng:
            dir = dirs[dirs_idx]
            next_row, next_col = current_row+dir[0], current_col+dir[1]
            print(next_row, next_col)
            if next_row < 0 or next_row > m - 1 or next_col < 0 or next_col > n - 1 or visited[next_row][next_col] == 1:
                dirs_idx = 0 if (dirs_idx + 1) % 4 == 0 else dirs_idx + 1
            else:
                current_row, current_col = next_row, next_col
                visited[current_row][current_col] = 1
                path.append(matrix[current_row][current_col])
        return path

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirs_idx = 0
        m, n = len(matrix), len(matrix[0])
        lng = m * n
        visited = [[0 for _ in range(n)] for _ in range(m)]
        path = []
        current_row, current_col = 0, 0
        visited[current_row][current_col] = 1
        path.append(matrix[current_row][current_col])
        while len(path) < lng:
            dir = dirs[dirs_idx]
            next_row, next_col = current_row+dir[0], current_col+dir[1]
            if next_row < 0 or next_row > m - 1 or next_col < 0 or next_col > n - 1 or visited[next_row][next_col] == 1:
                dirs_idx = 0 if (dirs_idx + 1) % 4 == 0 else dirs_idx + 1
            else:
                current_row, current_col = next_row, next_col
                visited[current_row][current_col] = 1
                path.append(matrix[current_row][current_col])
        return path


tcs = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
]
for tc in tcs:
    sol = Solution().spiralOrder(tc)
    print(sol)
