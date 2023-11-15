from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        if len(bank) == 0:
            return -1

        def diff(a, b):
            di = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    di += 1
            return di
        # index, depth
        queue = [(0, startGene)]
        while len(queue) != 0:
            c_d, c = queue.pop()
            if c == endGene:
                return c_d
            for b in bank[:]:
                if diff(c, b) == 1:
                    queue.append((c_d+1, b))
                    bank.remove(b)
        return -1


# tcs = [
#     {
#         "startGene": "AACCGGTT",
#         "endGene": "AACCGGTA",
#         "bank": ["AACCGGTA"]
#     },
#     {
#         "startGene": "AACCGGTT",
#         "endGene": "AAACGGTA",
#         "bank": ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#     }
# ]
# for tc in tcs:
