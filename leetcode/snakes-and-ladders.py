from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = []
        visited = {}
        n = len(board)
        queue.append((1, 0))
        while len(queue) != 0:
            current, current_depth = queue.pop(0)  # TODO Dequeue로 바꾸면 조금 나음
            if current in visited:
                continue
            else:
                visited[current] = True
            if current == n * n:
                return current_depth
            next = self.getNext(current, n)
            for i in range(next[0], next[1]+1):
                co = self.getCoordinate(i, n)
                if board[co[0]][co[1]] != -1:
                    next_co = board[co[0]][co[1]]
                    if not next_co in visited:
                        queue.append((next_co, current_depth+1))
                else:
                    if not i in visited:
                        queue.append((i, current_depth+1))
        return -1

    def snakesAndLaddersWrongButConcept(self, board: List[List[int]]) -> int:
        queue = []
        n = len(board)
        queue.append(1)
        cnt = -1
        while len(queue) != 0:
            cnt += 1
            current = queue.pop(0)  # TODO Dequeue로 바꾸면 조금 나음
            print('current: ', current)
            if current == n * n:
                return cnt
            next = self.getNext(current, n)
            flag = False
            # check final
            if next[1] == n*n:
                queue.append(n*n)
                continue
            for i in range(next[0], next[1]+1):
                co = self.getCoordinate(i, n)
                print('compare: ', co, board[co[0]][co[1]])
                if board[co[0]][co[1]] != -1:
                    next_co = board[co[0]][co[1]]
                    print('current:', self.getCoordinate(
                        current, n), ' to next:', co, '. so that can use ladder or snake.', self.getCoordinate(next_co, n))
                    queue.append(next_co)
                    flag = True
                    break
            if not flag:
                i = self.getNext(current, n)[1]
                print('current:', self.getCoordinate(
                    current, n), ' to next:', self.getCoordinate(i, n))
                queue.append(i)
        return cnt

    def getNext(self, curr: int, n: int) -> [int, int]:
        return [curr + 1, min(curr + 6, n*n)]

    def getCoordinate(self, cur: int, n: int) -> (int, int):
        row = (n*n - cur) // n
        col = ((cur - 1) % n)
        if (n-row) % 2 == 0:
            col = n - 1 - col
        return (row, col)


tcs = [
    [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1],
     [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]],
    [[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]],
    [[-1, -1],
     [-1, 3]],
    [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]
]


# sol = Solution().getCoordinate(9, 3)
for tc in tcs:
    sol = Solution().snakesAndLadders(tc)
    print(sol)
