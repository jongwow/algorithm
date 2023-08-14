from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        idx_x, idx_y = 0, 0
        s = set([])
        while idx_x < 9:
            idx_y = 0
            while idx_y < 9:
                if board[idx_y][idx_x] == ".":
                    idx_y += 1
                    continue
                # square check
                square_namespace = str(idx_x // 3) + str(idx_y // 3)
                square_index = square_namespace+board[idx_y][idx_x]
                if square_index in s:
                    return False
                s.add(square_index)
                # col check
                col_namespace = "c"+str(idx_x)
                col_index = col_namespace + board[idx_y][idx_x]
                if col_index in s:
                    return False
                s.add(col_index)
                # row check
                row_namespace = "r"+str(idx_y)
                row_index = row_namespace + board[idx_y][idx_x]
                if row_index in s:
                    return False
                s.add(row_index)
                idx_y += 1
            idx_x += 1
        return True
