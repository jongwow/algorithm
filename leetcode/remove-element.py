from typing import List


class Solution:
    def removeElement_v1(self, nums: List[int], val: int) -> int:
        nums.sort()
        i = 0
        dup = -1
        cnt = 0
        while i < len(nums):
            if nums[i] == val:
                if dup == -1:
                    dup = i
                cnt += 1
            i += 1
        total = len(nums) - cnt
        a = dup
        b = dup + cnt
        i = 0
        while i < cnt:
            i += 1
            nums.pop(dup)
        return total

    def removeElement_v2(self, nums: List[int], val: int) -> int:
        i = 0
        ori = len(nums)
        cnt = 0
        while i < len(nums):
            # print('i: ', i, ', cur: ', nums[i], ', len: ', len(nums))
            if nums[i] == val:
                cnt += 1
                popped = nums.pop(i)
                # print('pop:', popped)
                continue
            i += 1
        # print('result:', nums)
        return ori - cnt

    def removeElement_v3(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


sol = Solution()
my_nums = [0, 1, 2, 2, 3, 0, 4, 2]
ans = sol.removeElement_v2(my_nums, 2)
print(ans)
print(my_nums)
