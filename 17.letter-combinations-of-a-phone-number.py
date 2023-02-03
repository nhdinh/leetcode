#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
import itertools
from typing import List

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []

        combinations = itertools.product(*(keys[d] for d in digits))

        return [''.join(x) for x in combinations]

        
# @lc code=end

