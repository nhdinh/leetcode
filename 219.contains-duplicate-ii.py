# 219. Contains Duplicate II
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        l = len(nums)

        for i in range(l):
            if nums[i] in d:
                if abs(i - d[nums[i]]) <= k:
                    return True

            d[nums[i]] = i

        return False
