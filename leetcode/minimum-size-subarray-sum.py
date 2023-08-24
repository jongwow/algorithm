from typing import List
from sys import maxsize


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_nums = len(nums)
        l, r = 0, 0
        sum = 0
        ans = maxsize
        while r < len_nums:
            sum = nums[r] + sum
            while sum >= target:
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
        return ans if ans != maxsize else 0

    def minSubArrayLenWIP(self, target: int, nums: List[int]) -> int:
        len_nums = len(nums)
        p_s = []
        p_s.append([0, 0])
        idx = 1
        while idx <= len_nums:
            p_s.append([idx, nums[idx-1] + p_s[idx-1][1]])
            idx += 1
        print(p_s)
        idx = 0
        p_s2 = []
        while idx < len_nums+1:
            inner_idx = 0
            while inner_idx < idx:
                p_s[idx]-p_s[inner_idx]
                p_s2.append(- target)
                inner_idx += 1
            idx += 1
        p_s2.sort()

        return 0

    def minSubArrayLenTimeLimit3(self, target: int, nums: List[int]) -> int:
        len_nums = len(nums)
        p_s = [0] * (len_nums + 1)
        idx = 1
        p_s[0] = 0
        ans = []
        while idx <= len_nums:
            p_s[idx] = nums[idx-1] + p_s[idx-1]
            inner_idx = idx - 1
            while inner_idx >= 0:
                sum = p_s[idx] - p_s[inner_idx]
                if sum >= target:
                    ans.append(idx-inner_idx)
                    break
                inner_idx -= 1
            idx += 1
        ans.sort()
        if len(ans) == 0:
            return 0
        return ans[0]

    def minSubArrayLenTimeLimit2(self, target: int, nums: List[int]) -> int:
        len_nums = len(nums)
        p_s = [0] * (len_nums + 1)
        idx = 1
        p_s[0] = 0
        while idx <= len_nums:
            p_s[idx] = nums[idx-1] + p_s[idx-1]
            idx += 1
        window = 1
        while window <= len_nums:
            start = 0
            while start <= len_nums - window:
                sum = p_s[start+window] - p_s[start]
                if sum >= target:
                    return window
                start += 1
            window += 1
        return 0

    def minSubArrayLenTimeLimit(self, target: int, nums: List[int]) -> int:
        window_size = 0
        len_nums = len(nums)
        while window_size < len_nums:
            window_size += 1
            print('window_size: ', window_size)
            start = 0
            while start <= len_nums - window_size:
                print('-- start: ', start)
                idx = start
                sum = 0
                while idx < start + window_size:
                    print('--- idx: ', idx)
                    sum += nums[idx]
                    idx += 1
                start += 1
                if sum >= target:
                    return window_size
        return 0


# tc = [7, [2, 3, 1, 2, 4, 3]]
# tc = [4, [1, 4, 4]]
# tc = [11, [1, 1, 1, 1, 1, 1, 1, 1]]
tc = [15, [1, 2, 3, 4, 5]]

ans = Solution().minSubArrayLen(tc[0], tc[1])
print(ans)
