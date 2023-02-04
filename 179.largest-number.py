#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

from typing import List

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        # since 0 <= nums[i] <= 10^9, the largest number is 10**9 will have 10 digits, therefore
        # str(22...22) > str(1010...1010)
        nums.sort(key=lambda x: x*9, reverse=True)
        return str(int(''.join(nums)))
        
# @lc code=end

