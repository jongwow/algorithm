import math
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        return self.minimumCardPickup_HashMap_V2(cards)

    def minimumCardPickup_HashMap(self, cards: List[int]) -> int:
        dict1 = dict()
        dist = dict()
        for cardIndex in range(len(cards)):
            card = cards[cardIndex]
            if card in dict1:
                if not (card in dist):
                    dist[card] = math.inf
                cd = cardIndex - dict1[card]
                dist[card] = dist[card] if dist[card] < cd else cd
            dict1[card] = cardIndex
        mini = math.inf
        has = False
        for cardIndex in range(len(cards)):
            card = cards[cardIndex]
            if card in dist:
                if dist[card] != 0 and mini > dist[card]:
                    mini = dist[card]
                    has = True
        if has:
            return mini+1
        else:
            return -1

    def minimumCardPickup_HashMap_V2(self, cards: List[int]) -> int:
        my_dict = dict()
        ans = math.inf
        for c_id in range(len(cards)):
            card = cards[c_id]
            if (card in my_dict):
                dif = c_id - my_dict[card]
                if dif < ans:
                    ans = dif
            my_dict[card] = c_id

        if ans == math.inf:
            return -1
        else:
            return ans+1


if __name__ == "__main__":
    test_cases = [
        [3, 4, 2, 3, 4, 7],
        [1, 0, 5, 3],
        [95, 11, 8, 65, 5, 86, 30, 27, 30, 73, 15, 91, 30,
            7, 37, 26, 55, 76, 60, 43, 36, 85, 47, 96, 6],
    ]
    test_outs = [
        4,
        -1,
        3
    ]
    for i in range(len(test_cases)):
        ca = test_cases[i]
        output = Solution().minimumCardPickup(ca)
        expected = test_outs[i]
        print()
        if output == expected:
            print('Correct!')
        else:
            print('Wrong!')
            print('{0} != {1}'.format(expected, output))
