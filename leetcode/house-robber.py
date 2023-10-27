
from typing import List


class Solution:
    # 14m 21s
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*100001
        l = len(nums)

        def solve(nums, st, en):
            print(st, en)
            idx = st*100+en
            # base case
            if dp[idx] != -1:
                return dp[idx]
            # base case2
            # - 범위 밖 -> end of loop
            if st == en:
                return nums[st]
            if st > en:  # 1만큼 큰 경우만 있겠지.
                return 0
            # recursive case
            # - dp[] = max(st를 뽑을 경우, st를 안뽑을 경우)
            case_a = nums[st] + solve(nums, st+2, en)
            case_b = solve(nums, st+1, en)
            dp[idx] = max(case_a, case_b)
            return dp[idx]
        ans = solve(nums, 0, l-1)
        return ans


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*101
        l = len(nums)

        def solve(st):
            # print(st)
            idx = st
            # base case
            if dp[idx] != -1:
                return dp[idx]
            # base case2
            # - 범위 밖 -> end of loop
            if st == l-1:
                return nums[st]
            if st > l-1:  # 1만큼 큰 경우만 있겠지.
                return 0
            # recursive case
            # - dp[] = max(st를 뽑을 경우, st를 안뽑을 경우)
            case_a = nums[st] + solve(st+2)
            case_b = solve(st+1)
            dp[idx] = max(case_a, case_b)
            return dp[idx]
        ans = solve(0)
        return ans


sol = Solution()
tcs = [
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

]
for tc in tcs:
    print(sol.rob(tc))
