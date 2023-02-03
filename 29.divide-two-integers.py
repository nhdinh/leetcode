#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        neg = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        for i in range(31, -1, -1):
            if dividend >> i >= divisor:
                ans += 1 << i
                dividend -= divisor << i

        if neg:
            ans = -ans

        return min(max(-2147483648, ans), 2147483647)
        
# @lc code=end

