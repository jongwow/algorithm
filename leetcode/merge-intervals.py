from typing import List

# 2339 ~ 00:02, 0040 ~


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda st: st[0])
        left = 0
        START, END = 0, 1
        result = []
        prev_start = -1
        prev_end = -1
        while left < len(intervals):
            if prev_end != -1:
                if intervals[left][START] <= prev_end:
                    # print('intervals[', left, '] : ',
                    #       intervals[left][START], '<=', prev_end)
                    prev_end = max(intervals[left][END], prev_end)
                    left += 1
                    continue
                else:
                    # print('intervals[', left, '] : ',
                    #       intervals[left][START], '>', prev_end)
                    # print('-- inserting result', prev_start, prev_end)
                    result.append([prev_start, prev_end])
                    prev_start, prev_end = intervals[left][START], intervals[left][END]
                    left += 1
                    continue
            else:
                prev_start, prev_end = intervals[left][START], intervals[left][END]
                left += 1
                continue
        result.append([prev_start, prev_end])
        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda st: st[0])
        left = 0
        START, END = 0, 1
        result = []
        prev_start = -1
        prev_end = -1
        while left < len(intervals):
            if prev_end != -1:
                if intervals[left][START] <= prev_end:
                    prev_end = max(intervals[left][END], prev_end)
                    left += 1
                    continue
                else:
                    result.append([prev_start, prev_end])
                    prev_start, prev_end = intervals[left][START], intervals[left][END]
                    left += 1
                    continue
            else:
                prev_start, prev_end = intervals[left][START], intervals[left][END]
                left += 1
                continue
        result.append([prev_start, prev_end])
        return result
        # intervals 의 시작 시간 기준으로 정렬.
        # left를 앞에서부터 순회 ~ 끝-1 이전까지

        # 만약 종료후보시간이 있다면
        #   현재주기의 시작시간이 종료후보시간보다 같거나 이전이라면(오버래핑)
        #       현재주기의 종료시간과 종료후보시간 중 더 큰 값을 종료후보시간으로 설정
        #       continue
        #   현재주기의 시작시간이 종료후보시간보다 이후라면
        #       (이전) 시작후보시간 ~ 종료후보시간을 정답처리.
        #       현재주기의 시작시간을 시작후보시간으로 재설정, 현재주기의 종료시간을 종료후보시간으로 재설정
        #       continue
        # 만약 종료후보시간이 없다면
        #   현재주기의 시작시간을 시작후보시간으로 재설정, 현재주기의 종료시간을 종료후보시간으로 재설정
        #   continue


tcs = [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]]
    # [[2, 6], [15, 18], [8, 10], [1, 3]]
]
for tc in tcs:
    new_tc = sorted(tc, key=lambda st: st[0])
    sol = Solution().merge(new_tc)
    print(sol)
