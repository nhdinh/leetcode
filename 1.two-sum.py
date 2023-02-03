#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort nums ascending without losing index
        nums = [(k,n) for k,n in enumerate(nums)]
        nums.sort(key=lambda x: x[1])

        # move 2 pointers from both ends
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i][1] + nums[j][1] == target:
                return [nums[i][0], nums[j][0]]
            elif nums[i][1] + nums[j][1] < target:
                i += 1
            else:
                j -= 1
        
        return None
        
# @lc code=end

