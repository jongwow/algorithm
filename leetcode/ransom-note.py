from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for ch in magazine:
            if ch in dictionary:
                dictionary[ch] += 1
            else:
                dictionary[ch] = 1
        for ch in ransomNote:
            if ch in dictionary:
                dictionary[ch] -= 1
                if dictionary[ch] == 0:
                    del dictionary[ch]
            else:
                return False
        return True


# inputs = ["a", "b"]
inputs = ["aa", "ab"]
inputs = ["aa", "aab"]
sol = Solution().canConstruct(inputs[0], inputs[1])
print(sol)
