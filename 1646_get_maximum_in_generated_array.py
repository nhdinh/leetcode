# 1646. Get Maximum in Generated Array
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def maxi(i, nums={}):
            if i == 0 or i == 1:
                return i

            j = i//2
            if j*2 == i and 2 <= i <= n and i not in nums:
                nums[i] = maxi(j, nums)
            elif j*2+1 == i and 2 <= i <= n and i not in nums:
                nums[i] = maxi(j, nums) + maxi(j+1, nums)

            return nums[i]

        nums = {}
        nnn = [maxi(i, nums) for i in range(n+1)]
        return max(nnn)
