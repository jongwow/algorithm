from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = min(height[0], height[1])
        if len(height) == 2:
            return ans
        prev_idx = 0
        for idx, h in enumerate(height):
            print(idx, h)
        return 4

    def maxArea_v1(self, height: List[int]) -> int:
        ans = min(height[0], height[1])
        if len(height) == 2:
            return ans
        s = 0
        e = len(height)-1
        while s < e:
            w = e - s
            h = min(height[s], height[e])
            if height[e] < height[s]:
                e -= 1
            else:
                s += 1
            ans = max(ans, w * h)
        return ans


tcs = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1, 1]
]
for tc in tcs:
    sol = Solution().maxArea_v1(tc)
    print(sol)
