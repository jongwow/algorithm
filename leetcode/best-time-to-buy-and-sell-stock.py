from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # where you buy
        right = 1  # where you sell
        result = 0
        len_prices = len(prices)
        while right < len_prices:
            pr = prices[right]
            pl = prices[left]
            if result < pr - pl:
                result = pr - pl
            if pr < pl:
                left = right
            right += 1
        return result
