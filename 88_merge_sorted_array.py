# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nn = nums1[:m] + nums2[:n]
        del nums1[::]
        nums1 += sorted(nn)