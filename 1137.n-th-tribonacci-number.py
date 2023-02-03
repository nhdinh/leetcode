# 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int, nums={}) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            if n not in nums:
                nums[n] = self.tribonacci(
                    n-3, nums) + self.tribonacci(n-2, nums) + self.tribonacci(n-1, nums)

            return nums[n]
