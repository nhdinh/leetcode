# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur_idx = -1
        for c in list(s):
            c_idx = t.find(c, cur_idx + 1)
            print(c, ", c_idx = ", c_idx)

            if c_idx > cur_idx + 1:
                cur_idx = c_idx
            else:
                return False

        return True
