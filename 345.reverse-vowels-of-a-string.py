#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in v:
                i += 1
            elif s[j] not in v:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
        
# @lc code=end

