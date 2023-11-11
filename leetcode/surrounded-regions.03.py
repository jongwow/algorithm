from typing import List

# visited = [] 동일한 크기

# 순회하면서 O
# DFS. O 를 C로 바꾸면 visited.
# C를 돌면서 벽을 만나면 이건 그대로 O로 해야함.
# C를 돌면서 벽을 만나지 않고 다 돌면 C를 X로 바꿔줌.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]
        len_i = len(board)
        len_j = len(board[0])
        q = []
        p = []
        for i in range(len_i):
            for j in range(len_j):
                if board[i][j] == 'O':
                    q.append((i, j))
                    escape = False
                    while len(q) != 0:
                        c_i, c_j = q.pop()
                        p.append((c_i, c_j))
                        board[c_i][c_j] = 'X'
                        for dd in d:
                            n_i, n_j = c_i + dd[0], c_j + dd[1]
                            if n_i < 0 or n_i >= len_i or n_j < 0 or n_j >= len_j:
                                escape = True
                            elif board[n_i][n_j] == 'O':
                                q.append((n_i, n_j))
                    if escape:
                        while len(p) != 0:
                            c = p.pop()
                            board[c[0]][c[1]] = 'O'
                    else:
                        p = []
        print(board)
        return ""


tcs = [
    [["X", "X", "X", "X"], ["X", "O", "O", "X"], [
        "X", "X", "O", "X"], ["X", "O", "X", "X"]],
    [["X"]],
    [["X", "X", "X", "X"], ["X", "O", "O", "X"], [
        "X", "X", "O", "X"], ["X", "O", "X", "X"]]


]
for tc in tcs:
    ans = Solution().solve(tc)
    print()
