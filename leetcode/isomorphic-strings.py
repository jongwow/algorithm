from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s = len(s)
        val_s = [0 for i in range(128)]
        val_t = [0 for i in range(128)]
        idx = 0
        gap = 1
        while idx < len_s:
            ord_s = ord(s[idx])
            ord_t = ord(t[idx])
            if val_s[ord_s] != val_t[ord_t]:
                return False
            val_s[ord_s] = idx + gap
            val_t[ord_t] = idx + gap
            idx += 1
        return True

    def isIsomorphicV2(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len(s) != len(t):
            return False
        dic = {}
        used = set([])
        idx = 0
        while idx < len_s:
            ch = s[idx]
            target = ord(t[idx])
            if not ch in dic:
                if target in used:  # 중복해서 넣는다면?
                    return False
                else:
                    used.add(target)
                dic[ch] = target
            else:  # 이미 있음
                if dic[ch] != target:
                    return False
            idx += 1
        new_s = ""
        for c in s:
            new_s += chr(dic[c])
        return t == new_s

    def isIsomorphicV1(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len(s) != len(t):
            return False
        ord_t = [ord(c) for c in t]
        diction = {}  # ord_s: ord_c 매핑
        idx = 0
        while idx < len_s:
            oc = ord(s[idx])
            if not oc in diction:
                diction[oc] = ord_t[idx]
            elif diction[oc] != ord_t[idx]:
                return False
            else:
                pass
            idx += 1
        new_diction = {}
        for d in diction:
            if diction[d] in new_diction and new_diction[diction[d]] != d:
                return False
            new_diction[diction[d]] = d
        return True


tcs = [
    ["badc", "baba"],
    ["bbbaaaba", "aaabbbba"],
    ["egg", "add"]
]
for tc in tcs:
    sol = Solution().isIsomorphic(tc[0], tc[1])
    sol2 = Solution().isIsomorphicV1(tc[0], tc[1])
    print("answer:", sol2, ", output:", sol)
