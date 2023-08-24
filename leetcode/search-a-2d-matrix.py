from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchMatrixUsingIndexer(matrix, target)

    def searchMatrixUsingIndexer(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        st = 0
        en = m * n - 1
        while en - st >= 0:
            mid = (en + st) // 2
            mid_n = mid // m
            mid_m = mid - mid_n * m
            if matrix[mid_n][mid_m] == target:
                return True
            elif matrix[mid_n][mid_m] < target:
                st = mid + 1
            else:
                en = mid - 1
        return False


# for i in range(12):
#     print(indexer(4, 3, i))  # 0, 1


tcs = [
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13]
]

for tc in tcs:
    sol = Solution().searchMatrix(tc[0], tc[1])
    print(sol)
