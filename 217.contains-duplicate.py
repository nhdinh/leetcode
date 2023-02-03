# 217. Contains Duplicate
import collections
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        return any(c[n] >= 2 for n in set(nums))
