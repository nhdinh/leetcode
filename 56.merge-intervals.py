#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

from typing import List

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0]) # O(n)
        ret = []
        
        for interval in intervals: # O(n)
            if len(ret) == 0 or interval[0] not in range(ret[-1][0], ret[-1][1]+1):
                ret.append(interval)
            else:
                if interval[0] in range(ret[-1][0], ret[-1][1]+1):
                    ret[-1] = [ret[-1][0], max(ret[-1][1], interval[1])]
                else:
                    ret.append(interval)
            
        return ret
        
# @lc code=end

