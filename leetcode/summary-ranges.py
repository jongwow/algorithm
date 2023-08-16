from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        len_nums = len(nums)
        if len_nums == 0:
            return []
        if len_nums == 1:
            return [str(nums[0])]
        idx = 1
        start = nums[idx-1]
        end = nums[idx-1]
        result = []
        while idx < len_nums:
            # print(nums[idx-1], nums[idx], idx)
            if nums[idx] - nums[idx-1] == 1:
                end = nums[idx]
            else:
                # print('start:', start, ', end:', end)
                if start == end:
                    result.append(str(start))
                else:
                    result.append("{}->{}".format(start, end))
                start = nums[idx]
                end = nums[idx]
            # 이전과 지금이 1차이라면
            # end를 지금으로 바꿈.
            # 이전과 지금이 1 차이가 아니라면
            # 결과에 넣고,
            # start를 지금으로, end를 지금으로 바꿈.
            idx += 1
        if start == end:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, end))
        return result

    def summaryRangesV1(self, nums: List[int]) -> List[str]:
        len_nums = len(nums)
        if len_nums == 0:
            return []
        if len_nums == 1:
            return [str(nums[0])]
        idx = 1
        start = nums[idx-1]
        end = nums[idx-1]
        result = []
        while idx < len_nums:
            if nums[idx] - nums[idx-1] == 1:
                end = nums[idx]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append("{}->{}".format(start, end))
                start = nums[idx]
                end = nums[idx]
            idx += 1
        if start == end:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, end))
        return result

    def summaryRangesV1Refactor(self, nums: List[int]) -> List[str]:
        result = []
        len_nums = len(nums)
        if len_nums == 0:
            return []
        idx = 1
        start = nums[idx-1]
        end = nums[idx-1]
        result = []
        while idx < len_nums:
            if nums[idx] - nums[idx-1] != 1:
                if start == end:
                    result.append(str(start))
                else:
                    result.append("{}->{}".format(start, end))
                start = nums[idx]
            end = nums[idx]
            idx += 1
        if start == end:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, end))
        return result


tcs = [
    [0, 1, 2, 4, 5, 7],
    [0, 2, 3, 4, 6, 8, 9],
    [1]
]

for tc in tcs:
    sol = Solution().summaryRanges(tc)
    sol2 = Solution().summaryRangesV1Refactor(tc)
    print(sol)
    print(sol2)
