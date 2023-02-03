# 121. Best Time to Buy and Sell Stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)

        def maxSellPrice(buying_day: int, msp={}):
            if buying_day >= l - 1:
                return 0
            else:
                m = max(maxSellPrice(buying_day + 1, msp),
                        prices[buying_day+1])
                msp[buying_day] = m
                return m

        return max([maxSellPrice(i) - prices[i] for i in range(l-1, -1, -1)])
