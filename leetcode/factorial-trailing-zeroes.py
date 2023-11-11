import math


class Solution:
    def trailingZeroesWrong1(self, n: int) -> int:
        if n == 0:
            return 0
        ans = 1
        while n >= 1:
            ans = ans * n
            n = n - 1
        cnt = 0
        print(ans)
        print()
        while ans % 10 == 0:
            print(ans)
            print(ans/10)
            print("{:f}".format(ans/10))

            print('-')
            ans = ans // 10
            cnt += 1
        return cnt

    # 11m 48s
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        c_2 = 0
        c_5 = 0
        while n >= 1:
            nn = n
            while nn >= 1:
                if nn % 2 != 0:
                    break
                c_2 += 1
                nn = math.floor(nn / 2)
            nn = n
            while nn >= 1:
                if nn % 5 != 0:
                    break
                c_5 += 1
                nn = math.floor(nn / 5)
            n -= 1
        return min(c_2, c_5)

    def trailingZeroesV2(self, n: int) -> int:
        if n == 0:
            return 0
        c_5 = 0
        while n >= 1:
            nn = n
            while nn >= 1:
                if nn % 5 != 0:
                    break
                c_5 += 1
                nn = math.floor(nn / 5)
            n -= 1
        return c_5


sol = Solution()
print(sol.trailingZeroesWrong1(30))
print(sol.trailingZeroesV2(30))
