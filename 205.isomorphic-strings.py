#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

from collections import Counter

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
            

        
# @lc code=end

