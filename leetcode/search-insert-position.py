from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        st = 0
        en = len(nums) - 1
        mid = 0
        while en - st >= 0:
            mid = (en + st) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                en = mid - 1  # - 1
            else:
                st = mid + 1  # + 1
        return st


tcs = [
    [[1, 3, 5, 6], 5, 2],
    [[1, 3, 5, 6], 2, 1],
    [[1, 3, 5, 6], 7, 4],
    [[1, 3, 5, 6], 0, 0],
    [[1, 3, 5, 6], 2, 1],
]
for tc in tcs:
    sol = Solution().searchInsert(tc[0], tc[1])
    if sol != tc[2]:
        print(tc[0], tc[1], tc[2], '!=', sol)
