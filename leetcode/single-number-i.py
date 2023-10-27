from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        return ans

    def singleNumberV1(self, nums: List[int]) -> int:
        bottom = min(nums)
        if bottom < 0:
            bottom = -bottom
        ans = 0
        for n in nums:
            ans ^= 1 << (n+bottom)
        # 2 = 10
        # 16  = 10000
        cnt = 0
        while ans:
            ans = ans >> 1
            cnt += 1
        return cnt-1-bottom


sol = Solution()
print(sol.singleNumber([2, 2, 7]))
print(sol.singleNumber([2, 2, 1]))
print(sol.singleNumber([4, 1, 2, 1, 2]))
print(sol.singleNumber([-1]))
