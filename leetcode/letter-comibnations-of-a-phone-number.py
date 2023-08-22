from typing import List


class Solution:
    def __init__(self) -> None:
        self.defined_table = {
            "2": [ch for ch in "abc"],
            "3": [ch for ch in "def"],
            "4": [ch for ch in "ghi"],
            "5": [ch for ch in "jkl"],
            "6": [ch for ch in "mno"],
            "7": [ch for ch in "pqrs"],
            "8": [ch for ch in "tuv"],
            "9": [ch for ch in "wxyz"],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.defined_table[digits[0]]
        letters = self.defined_table[digits[0]]
        result = []
        for ch in letters:
            rests = self.letterCombinations(digits[1:])
            for rest in rests:
                result.append(ch + rest)
        return result


class SolutionV1:
    def __init__(self) -> None:
        self.defined_table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = self.bk(digits)
        # print("res: ", res)
        return res

    def bk(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.get_letters(digits[0])

        letters = self.bk(digits[0])
        # print("letters of", digits[0], ": ", letters)
        result = []
        for ch in letters:
            rests = self.bk(digits[1:])
            for rest in rests:
                result.append(ch + rest)
        return result

    def get_letters(self, digit: str) -> List[str]:
        s = self.defined_table[digit]
        return [ch for ch in s]


tcs = [
    "23",
    "",
    "2"
]
for tc in tcs:
    sol = Solution().letterCombinations(tc)
    print(sol)

# print(Solution().get_letters("2"))
# print(Solution().get_letters("3"))
# print(Solution().get_letters("4"))
# print(Solution().get_letters("5"))
# print(Solution().get_letters("6"))
# print(Solution().get_letters("7"))
# print(Solution().get_letters("8"))
# print(Solution().get_letters("9"))
