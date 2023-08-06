from typing import List


class Solution:
    def majorityElement_v1(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        maj = len(nums) / 2 - 0.5
        if maj == 0:
            return nums[0]
        i = 0
        while i < (len(nums) - 1):
            if nums[i] == nums[i+1]:
                cnt += 1
                if cnt >= maj:
                    return nums[i]
            else:
                cnt = 0
            i += 1

    def majorityElement_v2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement_v3(self, nums: List[int]) -> int:
        maj = len(nums) // 2
        ma = {}
        for n in nums:
            if ma.get(n) is not None:
                ma[n] += 1
                if ma[n] > maj:
                    return n
            else:
                ma[n] = 1
        return nums[0]

    def majorityElement_v4(self, nums: List[int]) -> int:
        cnt = 0
        candidate = nums[0]
        i = 0
        while i < len(nums):
            print('i', i)
            if cnt == 0:
                print('boom')
                candidate = nums[i]
                cnt += 1
                i += 1
                continue
            if candidate == nums[i]:
                cnt += 1
            else:
                cnt -= 1
            i += 1
        print('cnt', cnt)
        return candidate

    def majorityElement_v5(self, nums: List[int]) -> int:
        cnt = 0
        candidate = nums[0]
        for n in nums:
            if cnt == 0:
                candidate = n
            if n == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate


sol = Solution()
ans = sol.majorityElement_v5([6, 5, 5])
print(ans)
