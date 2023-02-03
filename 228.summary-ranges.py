#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

from typing import List

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        d = [nums[k+1]-nums[k] for k in range(len(nums)-1)]
        ranges = []
        start = 0

        for _k, _r in enumerate(d):
            if _r != 1:
                ranges.append([nums[start], nums[_k]])
                start = _k+1

        if start < len(nums):
            ranges.append([nums[start], nums[-1]])
            
        return [f"{r[0]}->{r[1]}" if r[0] != r[1] else f"{r[0]}" for r in ranges]

        



        
# @lc code=end

