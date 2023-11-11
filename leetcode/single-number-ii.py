from typing import List

# 2 m 18 s


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     b_xor = 0
    #     b_or = 0
    #     b_or_or = 0
    #     b_or_or_or = 0
    #     for n in nums:
    #         if b_or & n == n:
    #             # print("duplicate:", n)
    #             if b_or_or & n == n:
    #                 # print('duplicated: duplicated: ', n)
    #                 b_or_or_or |= n  # 3번 이상
    #             b_or_or |= n  # 2번 이상
    #         b_or |= n  # 1번 이상
    #     print(b_or)
    #     print(b_or_or)
    #     print(b_or_or_or)
    #     return b_or ^ b_or_or ^ b_or_or_or
    def singleNumber(self, nums: List[int]) -> int:
        b_xor = 0
        b_and = 0
        b_or = 0
        for n in nums:
            if b_or & n == n:  # 1번 이상 발생한 건에 대해서
                if b_xor & n == n:  # 이미 기록했던 건이라면
                    pass
                b_xor ^= n
                b_or ^= n  # 기록했으니 제거한다.
            b_or |= n  # 1번 이상
        # print(b_or)
        # print(b_xor)
        return b_or ^ b_xor

    def singleNumber(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/single-number-ii/solutions/43296/an-general-way-to-handle-all-this-sort-of-questions/

        a = 0
        b = 0
        for n in nums:
            t = (~a & b & n) | (a & ~b & ~n)
            b = (~a & ~b & n) | (~a & b & ~n)
            a = t
        return a | b


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            if not (n in dic):
                dic[n] = 1

        for k in dic.keys():
            if dic[k] == 1:
                return k


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for c in nums:
            next_a = (~a & b & c) | (a & ~b & ~c)
            next_b = (~a & b & ~c) | (~a & ~b & c)
            a = next_a
            b = next_b
        return a | b


# more than 1 hour
# https://leetcode.com/problems/single-number-ii/solutions/43296/an-general-way-to-handle-all-this-sort-of-questions/
sol = Solution3()
print(sol.singleNumber([2, 2, 3, 2]))
print(sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))
print(sol.singleNumber([30, 5, 1, 30, 1, 30, 1]))
print(sol.singleNumber([30000, 500, 100, 30000, 100, 30000, 100]))
