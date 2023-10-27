from typing import List


class MyHeap:
    def __init__(self) -> None:
        self.heap = [None]
        self.size = 0

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        if self.size == 0:
            return
        current = len(self.heap) - 1
        parent = current // 2
        while current > 1 and self.heap[parent] < self.heap[current]:
            self.swap(current, parent)
            current = parent
            parent = current // 2


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        group = set(nums)
        ans = 1
        for n in nums:
            if n - 1 in nums:
                continue
            new_n = n + 1
            while new_n in group:
                new_n += 1
            ans = max(ans, new_n-n)
        return ans

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        a = 0
        for n in nums:
            if n - 1 not in nums:
                nn = n + 1
                while nn in nums:
                    nn += 1
                a = max(a, nn - n)
        return a

    def longestConsecutive_wrong(self, nums: List[int]) -> int:
        d = {}
        dd = {}
        idx = 0
        for n in nums:
            if n in d:
                continue
            if (n-1) in d and (n+1) in d:
                c = dd[d[n+1]] + dd[d[n-1]] + 1
                dd[d[n+1]] = dd[d[n-1]] = c
                d[n] = d[n+1]
            elif (n - 1) in d:
                d[n] = d[n-1]
                dd[d[n]] = dd[d[n]]+1
            elif (n + 1) in d:
                d[n] = d[n+1]
                dd[d[n]] = dd[d[n]]+1
            else:
                d[n] = idx
                dd[d[n]] = 1
                idx += 1
        print(d)
        print(dd.keys())
        print(dd.values())
        return max(dd.values())


tcs = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [0, -1]
]
for tc in tcs:
    ans = Solution().longestConsecutive(tc)
    print(ans)
