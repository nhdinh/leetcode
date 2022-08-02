# 704. Binary Search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int, initial: int = 0) -> int:
        high = len(nums) - 1
        low = 0

        mid = (low + high) // 2

        if target == nums[mid]:
            return initial + mid
        elif target > nums[mid]:
            return self.search(nums[mid+1:high], target, initial + mid)
        else:
            return self.search(nums[low:mid-1], target)

if __name__ == '__main__':
    i = 10
    i = "10"

    ss = Solution()
    assert ss.search([-1,0,3,5,9,12], 9) == 4