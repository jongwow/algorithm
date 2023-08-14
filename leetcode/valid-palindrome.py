from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            # skip condition
            if not s[l].isalnum():
                # print('s[l]', l, s[l])
                l += 1
                continue
            if not s[r].isalnum():
                # print('s[r]', r, s[r])
                r -= 1
                continue
            # print('l, r, s[l], s[r]', l, r, s[l], s[r])
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

    def isPalindrome_v2(self, s: str) -> bool:
        print(s)
        # Two Pointer
        l = 0
        r = len(s)-1
        while l < r:
            # skip condition
            if not s[l].isalnum():
                # print('s[l]', l, s[l])
                l += 1
                continue
            if not s[r].isalnum():
                # print('s[r]', r, s[r])
                r -= 1
                continue
            # print('l, r, s[l], s[r]', l, r, s[l], s[r])
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

    def isPalindrome_v1(self, s: str) -> bool:
        # sanitize
        new_string = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                new_string += c.lower()
        # print(new_string)
        # Two Pointer
        l = 0
        r = len(new_string)-1
        while l < r:
            if new_string[l] == new_string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


sol = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(sol)
sol = Solution().isPalindrome("race a car")
print(sol)
sol = Solution().isPalindrome(" ")
print(sol)
