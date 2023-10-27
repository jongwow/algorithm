from typing import List


class Solution:

    # 다른방법
    # 우선 가장 작은 값을 1로 만들자. 그리고 거기서 왼쪽, 오른쪽 계산해나가자.
    # - 순회하면서 가장 작은 값의 인데스를 찾는다.
    # - 그걸 기준으로 왼쪽 오른쪽 나눠서 보자.
    # -

    def candy_wrong(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        ans = 0
        # 레이팅이 큰 경우
        # - 전에 준 값보다 + 1
        # 같거나 작은 경우
        # - 전에 준 값보다 - 1

        # 엣지케이스
        # - 준에 준 값보다 - 1 했더니 0개야. 그러면 전체적으로 하나씩 더 줘야함.
        #
        candies = [0] * n
        candies[0] = 1
        idx = 1
        while idx < n:
            current = ratings[idx]
            if current > ratings[idx-1]:
                candies[idx] = candies[idx-1]+1
            else:
                if candies[idx-1] == 1:
                    inner_idx = 0
                    while inner_idx < idx:
                        candies[inner_idx] += 1
                        inner_idx += 1
                candies[idx] = 1
            idx += 1
        for n in candies:
            ans += n
        print(candies)

        # 개선 포인트
        # 처음부터 엄청 크게 주고 마지막에 sum = sum - n * (min+1)
        # - 엄청 크게 주고 = 1부터 2 * 10 ^ 4 까지의 합. = ((2 * 10 ^ 4) ^ 2) / 2 = 2 10 10 10 10 10 10 10 10s
        return ans

    def candy_wrong2(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        ans = 0
        candies = [0] * n
        candies[0] = 1
        idx = 1
        while idx < n:
            print(candies)
            current = ratings[idx]
            if current > ratings[idx-1]:
                candies[idx] = candies[idx-1]+1
            elif current == ratings[idx-1]:
                candies[idx] = 1
            else:
                if candies[idx-1] == 1:
                    inner_idx = idx-1
                    if inner_idx == 0:
                        candies[inner_idx] += 1
                    while inner_idx > 0:
                        # if candies[inner_idx-1] == candies[inner_idx]:
                        #     break
                        candies[inner_idx] += 1
                        if ratings[inner_idx-1] <= ratings[inner_idx]:
                            break
                        inner_idx -= 1
                candies[idx] = 1
            idx += 1
        for n in candies:
            ans += n
        print(candies)
        return ans

    def candy_time(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        ans = 0
        candies = [0] * n
        candies[0] = 1
        idx = 1
        while idx < n:
            print(idx)
            # print(candies)
            current = ratings[idx]
            if current > ratings[idx-1]:
                candies[idx] = candies[idx-1]+1
            elif current == ratings[idx-1]:
                candies[idx] = 1
            else:
                if candies[idx-1] == 1:
                    inner_idx = idx-1
                    candies[inner_idx] += 1
                    if inner_idx != 0:
                        while inner_idx > 0:
                            if ratings[inner_idx-1] > ratings[inner_idx] and candies[inner_idx-1] == candies[inner_idx]:
                                candies[inner_idx-1] += 1
                                inner_idx -= 1
                            elif ratings[inner_idx-1] > ratings[inner_idx] and candies[inner_idx-1] > candies[inner_idx]:
                                break
                            elif ratings[inner_idx-1] < ratings[inner_idx]:
                                break
                            elif ratings[inner_idx-1] == ratings[inner_idx]:
                                break
                            else:
                                # 발생할 수 있을까?
                                print("WTF")
                                break
                            # 더하고보니까, 그 전에 레이팅이 더 큰데 캔디는 같은 값을 갖네? 그러면 그 전에 레이팅이 더 컸던 값을 하나 더 더해줘야지
                            # 더하고보니까, 그 전에 레이팅이 더 큰데 캔디는 큰 값을 갖네? 빠져나와야지
                            # 더하고보니까, 그 전에 레이팅이 더 작네? 그러면 할게 없지 않나? 빠져나와야지
                            # 더하고보니까, 그 전에 레이팅이 같네? 그러면 할게 없지 않나? 빠져나와야지
                            # candies[inner_idx] += 1
                            # inner_idx -= 1
                candies[idx] = 1
            idx += 1
        for n in candies:
            ans += n
        # print(candies)
        return ans

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):  # i = n-2, n-3, ... 1, 0

            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)
# 73분 포기


tcs = [
    [1, 0, 2],  # 5
    [1, 2, 2],  # 4
    [1, 3, 2, 2, 1],  # 7 ([1, 2, 1, 2, 1])
    [1, 2, 3, 1, 0],  # 9 ([1, 2, 3, 2, 1])
    [1, 2, 87, 87, 87, 2, 1],  # 13 ([1, 2, 3, 1, 3, 2, 1])
]
for tc in tcs:
    sol = Solution()
    print(tc, '=> ')
    print(sol.candy(tc))
