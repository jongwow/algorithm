from typing import List


def equalList(a, b):
    if len(a) != len(b):
        return False
    idx = 0
    while idx < len(a):
        if a[idx] != b[idx]:
            return False
        idx += 1
    return True


def equalListList(a, b):
    if len(a) != len(b):
        return False
    idx = 0
    while idx < len(a):
        if not equalList(a[idx], b[idx]):
            return False
        idx += 1
    return True

# 1:50 실패.
# 겹치는 조건


def overlap(A, B):
    if A[0] < B[0] and A[1] < B[0]:
        return False
    if B[0] < A[0] and B[1] < A[0]:
        return False
    return True


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        FRONT = 0
        TAIL = 1
        new_front = 0
        new_tail = 0
        ans = []
        idx = 0
        l = len(intervals)
        if l == 0:
            return [newInterval]
        if newInterval[TAIL] < intervals[0][FRONT]:
            ans.append(newInterval)
            while idx < l:
                ans.append(intervals[idx])
                idx += 1
            return ans
        while idx < l and ((not overlap(newInterval, intervals[idx])) and (intervals[idx][TAIL] < newInterval[FRONT])):
            ans.append(intervals[idx])
            idx += 1
        if idx != l:
            new_front = min(intervals[idx][FRONT], newInterval[FRONT])
            while idx < l and overlap(newInterval, intervals[idx]):
                idx += 1
            # print('second: ', idx)
            new_idx_tail = idx
            new_tail = max(intervals[idx-1][TAIL], newInterval[TAIL])
            ans.append([new_front, new_tail])
            if idx == l:
                return ans
        else:    # 끝까지 갔을 때
            ans.append(newInterval)
            return ans
        while idx < l and not overlap(newInterval, intervals[idx]):
            ans.append(intervals[idx])
            idx += 1
        return ans


tcs = [
    [[1, 3], [2, 5], [[1, 5]]],
    [[1, 3], [4, 5], [[1, 3], [4, 5]]],
    [[1, 3], [6, 9], [2, 5], [[1, 5], [6, 9]]],
    [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16],
     [4, 8], [[1, 2], [3, 10], [12, 16]]],
    [[1, 5], [2, 6], [[1, 6]]],
    [[2, 5], [6, 7], [8, 9], [0, 1], [[0, 1], [2, 5], [6, 7], [8, 9]]],
    [[2, 4], [5, 6], [9, 10], [1, 10], [[1, 10]]],
    [[1, 5], [2, 3], [[1, 5]]],
    [[2, 5], [1, 4], [[1, 5]]],
    [[1, 5], [0, 3], [[0, 5]]],
    [[1, 5], [0, 5], [[0, 5]]],
    [[2, 6], [7, 9], [15, 18], [[2, 6], [7, 9], [15, 18]]],
    [[0, 5], [8, 9], [3, 4], [[0, 5], [8, 9]]],
    [[3, 5], [12, 15], [6, 6], [[3, 5], [6, 6], [12, 15]]],
]
for tca in tcs:
    # print(overlap([2, 5], [1, 3]))
    # print(equalListList([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    # continue
    tc = tca[:-1]
    ans = Solution().insert(tc[:-1], tc[-1])
    if not equalListList(ans, tca[-1]):
        print("False", ans, tca[-1])
    else:
        print("True")

    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     FRONT = 0
    #     TAIL = 1
    #     if len(intervals) == 0:
    #         return [newInterval]
    #     if len(intervals) == 1:
    #         if newInterval[TAIL] < intervals[0][FRONT]:
    #             return [newInterval, intervals[0]]
    #         elif intervals[0][TAIL] < newInterval[FRONT]:
    #             return [intervals[0], newInterval]
    #         elif newInterval[FRONT] < intervals[0][FRONT] and newInterval[TAIL] <= intervals[0][TAIL]:
    #             return [[newInterval[FRONT], intervals[0][TAIL]]]
    #         elif newInterval[FRONT] < intervals[0][FRONT] and newInterval[TAIL] < intervals[0][TAIL]:
    #             return [[newInterval[FRONT], intervals[0][TAIL]]]
    #         elif intervals[0][FRONT] <= newInterval[FRONT] and newInterval[TAIL] <= intervals[0][TAIL]:
    #             return intervals
    #         elif intervals[0][FRONT] <= newInterval[FRONT] and newInterval[TAIL] > intervals[0][TAIL]:
    #             return [[intervals[0][FRONT], newInterval[TAIL]]]
    #         if newInterval[TAIL] <= intervals[0][TAIL]:
    #             return []
    #     idx = 0
    #     new_intervals = []
    #     # 순회하다가
    #     while idx < len(intervals):
    #         while idx < len(intervals) and intervals[idx][FRONT] <= newInterval[FRONT]:
    #             new_intervals.append(intervals[idx])
    #             idx += 1
    #         start = idx
    #         if start == 0:
    #             new_front = newInterval[FRONT]
    #         else:
    #             if intervals[start-1][TAIL] < newInterval[FRONT]:
    #                 new_front = newInterval[FRONT]
    #             else:
    #                 new_intervals.pop()
    #                 new_front = intervals[start-1][FRONT]
    #         # print('start: ', start)
    #         while idx < len(intervals) and newInterval[TAIL] >= intervals[idx][TAIL]:
    #             idx += 1
    #         end = idx-1
    #         if end == 0:
    #             if newInterval[TAIL] <= intervals[end][TAIL]:
    #                 new_tail = intervals[end][TAIL]
    #             else:
    #                 new_tail = newInterval[TAIL]
    #         elif end == len(intervals):
    #             new_tail = newInterval[TAIL]
    #         else:
    #             if newInterval[TAIL] >= intervals[end][FRONT]:
    #                 # print('overlapped')
    #                 # print('newInterval[TAIL] >= intervals[end][FRONT]',
    #                 #       newInterval[TAIL], intervals[end][FRONT])
    #                 new_tail = intervals[end][TAIL]
    #                 idx += 1
    #             else:
    #                 # print('newInterval[TAIL] < intervals[end][FRONT]',
    #                 #       newInterval[TAIL], intervals[end][FRONT])
    #                 if newInterval[TAIL] < intervals[end][TAIL]:
    #                     new_tail = newInterval[TAIL]
    #                 else:
    #                     new_tail = intervals[end][TAIL]
    #         # print('new_front, new_tail:', new_front, new_tail)
    #         new_intervals.append([new_front, new_tail])
    #         while idx < len(intervals):
    #             # print(intervals[idx])
    #             new_intervals.append(intervals[idx])
    #             idx += 1
    #     return new_intervals

    # if newInterval[TAIL] < intervals[start][TAIL]:
    #     print('overlap')
    #     new_start = intervals[start]
    # else:
    #     new_start = intervals[FRONT]

    # def insert_bk_2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     FRONT = 0
    #     TAIL = 1
    #     if len(intervals) == 0:
    #         return [newInterval]
    #     idx = 0
    #     new_intervals = []
    #     # 순회하다가
    #     while idx < len(intervals):
    #         while intervals[idx][FRONT] <= newInterval[FRONT]:
    #             new_intervals.append(intervals[idx])
    #             idx += 1
    #         start = idx
    #         # print('start: ', start)
    #         while idx < len(intervals) and newInterval[TAIL] >= intervals[idx][TAIL]:
    #             idx += 1
    #         end = idx
    #         # print('end: ', end)
    #         if start == 0:
    #             new_front = newInterval[FRONT]
    #         else:
    #             if intervals[start-1][TAIL] < newInterval[FRONT]:
    #                 new_front = newInterval[FRONT]
    #             else:
    #                 # overlapped
    #                 new_intervals.pop()
    #                 new_front = intervals[start-1][FRONT]
    #         if end == len(intervals):
    #             new_tail = newInterval[TAIL]
    #         else:
    #             if newInterval[TAIL] <= intervals[end-1][FRONT]:
    #                 # overlapped
    #                 print('newInterval[TAIL] <= intervals[end-1][FRONT]',
    #                       newInterval[TAIL], '<= ', intervals[end-1][FRONT])
    #                 new_tail = intervals[end-1][TAIL]
    #                 idx += 1
    #             else:

    #                 print('newInterval[TAIL] > intervals[end-1][FRONT]',
    #                       newInterval[TAIL], '> ', intervals[end-1][FRONT])
    #                 new_tail = newInterval[TAIL]
    #         print('new_front, new_tail:', new_front, new_tail)
    #         new_intervals.append([new_front, new_tail])
    #         while idx < len(intervals):
    #             print(intervals[idx])
    #             new_intervals.append(intervals[idx])
    #             idx += 1
    #     return new_intervals

    # def insert_bk(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     FRONT = 0
    #     TAIL = 1
    #     if len(intervals) == 0:
    #         return [newInterval]
    #     idx = 0
    #     start_overlap = False
    #     end_overlap = False
    #     new_intervals = []
    #     # 순회하다가
    #     while idx < len(intervals):
    #         while intervals[idx][FRONT] <= newInterval[FRONT]:
    #             new_intervals.append(intervals[idx])
    #             idx += 1
    #         start = idx
    #         print('start: ', start)
    #         while idx < len(intervals) and newInterval[TAIL] >= intervals[idx][TAIL]:
    #             idx += 1
    #         end = idx
    #         print('end: ', end)
    #         if start == 0:
    #             new_front = newInterval[FRONT]
    #         else:
    #             if intervals[start-1][TAIL] < newInterval[FRONT]:
    #                 new_front = newInterval[FRONT]
    #             else:
    #                 # overlapped
    #                 new_front = intervals[start-1][FRONT]
    #         if end == len(intervals):
    #             new_tail = newInterval[TAIL]
    #         else:
    #             if newInterval[TAIL] <= intervals[end-1][FRONT]:
    #                 # overlapped
    #                 end_overlap = True
    #                 new_tail = intervals[end-1][TAIL]
    #             else:
    #                 new_tail = newInterval[TAIL]
    #         print(new_front, new_tail)
    #         while idx < len(intervals):
    #             new_intervals.append(intervals[idx])
    #             idx += 1
    #     return new_intervals
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     FRONT = 0
    #     TAIL = 1
    #     new_front = 0
    #     new_tail = 0
    #     ans = []
    #     idx = 0
    #     l = len(intervals)
    #     if l == 0:
    #         return [newInterval]
    #     if newInterval[TAIL] < intervals[0][FRONT]:
    #         ans.append(newInterval)
    #         while idx < l:
    #             ans.append(intervals[idx])
    #             idx += 1
    #         return ans
    #     while idx < l and not overlap(newInterval, intervals[idx]):
    #         ans.append(intervals[idx])
    #         idx += 1
    #     # case1) 종료
    #     new_idx_front = idx
    #     # print('first: ', idx)
    #     if idx == l:  # 끝까지 갔을 때
    #         # print('this is end of array')
    #         ans.append(newInterval)
    #         return ans
    #     # case2) idx 번째부터 겹치는 것.
    #     new_front = min(intervals[idx][FRONT], newInterval[FRONT])
    #     while idx < l and overlap(newInterval, intervals[idx]):
    #         idx += 1
    #     # print('second: ', idx)
    #     new_idx_tail = idx
    #     new_tail = max(intervals[idx-1][TAIL], newInterval[TAIL])
    #     # if new_idx_front == new_idx_tail-1:
    #     #     print("HERE")
    #     ans.append([new_front, new_tail])
    #     if idx == l:
    #         return ans
    #     while idx < l and not overlap(newInterval, intervals[idx]):
    #         ans.append(intervals[idx])
    #         idx += 1
    #     if idx != l:
    #         print("BROKEN!")
    #     return ans
