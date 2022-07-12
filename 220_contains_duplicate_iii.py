# 220. Contains Duplicate III
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        l = len(nums)
        nums = sorted([(i, nums[i]) for i in range(l)],
                      key=lambda e: e[1])  # a list of tuple

        i, j = 0, 0
        while i < l:
            while j < i and abs(nums[i][1] - nums[j][1]) > t:
                j += 1

            for mm in range(j, i):
                if abs(nums[mm][0] - nums[i][0]) <= k:
                    return True

            i += 1

        return False
