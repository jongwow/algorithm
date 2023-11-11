from typing import List


# 0041 0100
class Solution:
    def solve(self, nums: List[int]) -> int:
        p = [0, nums[0]]
        largest = nums[0]
        if p[0] < p[1]:
            smallest = p[0]
        else:
            smallest = p[1]
        for n in nums[1:]:
            cur = n+p[-1]
            p.append(cur)
            if largest < (cur - smallest):
                largest = cur - smallest
            if smallest > cur:
                print('smallest:', smallest, cur)
                smallest = cur

        print(p)
        print(smallest)
        return largest


sol = Solution()


res = sol.solve([-2, 1])
print(res)
