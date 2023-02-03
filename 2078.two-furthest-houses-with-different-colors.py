# 2078. Two Furthest Houses With Different Colors

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = len(colors)
        m = 0
        fc = 0 # first color
        
        for fc in range(l):
            for nc in range(l-1, fc, -1):
                if colors[fc] != colors[nc]:
                    m = max(m, nc - fc)
                    
        return m
        