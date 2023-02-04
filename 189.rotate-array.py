#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List
from collections import deque

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q = deque(nums)
        q.rotate(k)
        
        for i in range(len(q)):
            nums[i] = q[i]
        
# @lc code=end

