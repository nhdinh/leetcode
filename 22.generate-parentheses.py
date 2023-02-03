#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int, d={}) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            if n not in d:
                prev = self.generateParenthesis(n-1, d)
                cur = []
                for ps in prev:
                    for i in range(len(ps)):
                        new_ps = ps[0:i] + "()" + ps[i:len(ps)]
                        print(new_ps)

                        if new_ps not in cur:
                            cur.append(new_ps)

                d[n] = cur
            return d[n]

        
# @lc code=end

