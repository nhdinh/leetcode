#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

from typing import List

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _value(nums):
            return nums[0]*100+nums[1]*10+nums[2]

        def _swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        if nums[0] > nums[1] > nums[2]:
            nums.reverse()
            return

        if nums[0] < nums[1] < nums[2]:
            _swap(nums, 0, 2)
            return

        if nums[0] < nums[1] > nums[2]:
            _swap(nums, 1, 2)
            return

        if nums[0] > nums[1] < nums[2]:
            _swap(nums, 0, 1)
            return

        if nums[0] > nums[1] == nums[2]:
            _swap(nums, 0, 1)
            return

        if nums[0] == nums[1] < nums[2]:
            _swap(nums, 1, 2)
            return

        if nums[0] == nums[1] > nums[2]:
            _swap(nums, 0, 2)
            return

        if nums[0] < nums[1] == nums[2]:
            _swap(nums, 1, 2)
            return

        if nums[0] == nums[1] == nums[2]:
            return

        if nums[0] > nums[1] > nums[2]:
            nums.reverse()
            return

        
# @lc code=end

