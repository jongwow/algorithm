def romanChToInt(ch):
    # dic = {'I': 1, ...} => shorter
    if ch == 'I':
        return 1
    if ch == 'V':
        return 5
    if ch == 'X':
        return 10
    if ch == 'L':
        return 50
    if ch == 'C':
        return 100
    if ch == 'D':
        return 500
    if ch == 'M':
        return 1000


def compare_priority(ch_a: chr, ch_b: chr) -> bool:
    if romanChToInt(ch_a) < romanChToInt(ch_b):
        return True
    return False


class Solution:

    def romanToInt(self, s: str) -> int:
        # 현재 char 가 뒤따라오는 char보다 우선순위 낮다면?
        # - 현재 char를 -로 바꾸고, index++, calc(next)
        # 그렇지 않다면
        # - 현재 char를 +하고 index++;
        idx = 0
        summation = 0
        while idx < len(s):
            ch = s[idx]
            if idx + 1 < len(s):
                next_ch = s[idx + 1]
                if compare_priority(ch, next_ch):
                    summation = summation - romanChToInt(ch)
                    summation = summation + romanChToInt(next_ch)
                    idx = idx + 2
                else:
                    summation = summation + romanChToInt(ch)
                    idx = idx + 1
            else:
                summation = summation + romanChToInt(ch)
                idx = idx + 1
        return summation


solver = Solution()
print(solver.romanToInt("III"))
print(solver.romanToInt("LVIII"))
print(solver.romanToInt("MCMXCIV"))
print(solver.romanToInt("XXVII"))
