from typing import List


class Solution:

    # 16:05 ~ 16:10
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for st in strs:
            new_str = [*st]
            new_str.sort()
            new_str_key = ''.join(new_str)
            if new_str_key in results:
                results[new_str_key].append(st)
            else:
                results[new_str_key] = [st]

        return list(results.values())

    # 15:52 ~ 16:05
    def groupAnagramsTimeLimit(self, strs: List[str]) -> List[List[str]]:
        def createDict(st):
            res = {}
            for c in st:
                if c in res:
                    res[c] += 1
                else:
                    res[c] = 1
            return res

        def compareDict(a, b):
            a_keys = set(a)
            b_keys = set(b)
            if a_keys != b_keys:
                return False
            for a_key in a_keys:
                if a[a_key] != b[a_key]:
                    return False
            return True
        sets = []
        sets_cnt = []
        # hashMap
        for st in strs:
            new_set = createDict(st)
            found = False
            for prev_set_idx in range(len(sets)):
                if compareDict(sets[prev_set_idx], new_set):
                    sets_cnt[prev_set_idx].append(st)
                    found = True
                    break
            if not found:
                sets.append(new_set)
                sets_cnt.append([st])
        return sets_cnt


tcs = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [""],
    ["a"],
    ["ddddddddddg", "dgggggggggg"]
]

# 처음에 그냥 set으로 했다가 틀림

# 15:52 ~ 16:05
for tc in tcs:
    sol = Solution().groupAnagrams(tc)
    print(sol)
