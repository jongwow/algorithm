from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = self.subArray(nums, 0, len(nums)-1)
        return res

    def subArray(self, nums, low, high):
        if low > high:
            return -math.inf
        left, right = 0, 0
        mid = (low + high) // 2
        cur = 0
        for i in range(mid-1, low-1, -1):
            cur += nums[i]
            left = max(left, cur)
        cur = 0
        for i in range(mid+1, high+1):
            cur += nums[i]
            right = max(right, cur)
        return max(self.subArray(nums, low, mid-1), self.subArray(nums, mid+1, high), left + nums[mid]+right)

    def maxSubArrayV3(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dp = [0 for i in range(len_nums+1)]
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len_nums):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            res = max(res, dp[i])
        return res

    def maxSubArrayV2(self, nums: List[int]) -> int:
        len_nums = len(nums)
        ps = [0]
        sm = 0
        result = nums[0]-0
        for i in range(len_nums):
            ps.append(ps[i]+nums[i])
            gap = ps[i+1] - ps[sm]
            if result < gap:
                result = gap
            if ps[i+1] < ps[sm]:
                sm = i+1
        return result

    def maxSubArrayV1(self, nums: List[int]) -> int:
        len_nums = len(nums)
        ps = [0]
        for i in range(len_nums):
            ps.append(ps[i]+nums[i])
        idx = 1
        sm_idx = 0
        result = ps[1]-ps[0]
        while idx <= len_nums:
            # 지금까지 가장 작은 값과 현재 값을 뺼셈해서 갱신
            gap = ps[idx] - ps[sm_idx]
            if result < gap:
                result = gap
            # 0 <= < idx 중 가장 작은 값 찾기 = 지금까지 가장 작은 값과 현재 값을 비교
            if ps[idx] < ps[sm_idx]:
                sm_idx = idx
            idx += 1
        return result


tcs = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1],
    [5, 4, -1, 7, 8],
    [-1],
    [-2, -1],
    [-2, -1, -3],
    [-2, 0, -3, -3],
    [0, -3, 1, 1]
]
for tc in tcs:
    print(Solution().maxSubArray(tc))
    print('='*10)
