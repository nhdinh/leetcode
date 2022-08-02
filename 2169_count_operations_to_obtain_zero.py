# 2169. Count Operations to Obtain Zero

class Solution:
    def countOperations(self, n1, n2):
        ans = 0
        while n1 != 0 or n2 != 0:
            if n1 >= n2:
                n1 -= n2
            else:
                n2 -= n1

            ans += 1

        return ans