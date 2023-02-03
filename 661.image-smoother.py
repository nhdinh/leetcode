# 661. Image Smoother

import math
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]: 
        n, m = len(img[0]), len(img)
        if m == n == 1:
            return img
        
        def avg(i, j):
            s = 0
            c = 0
            for _i in range(i-1, i+2):
                for _j in range(j-1, j+2):
                    if 0 <= _i < m and 0 <= _j < n:
                        s += img[_i][_j]
                        c += 1
                        
            return math.floor(s/c)
        
        new_img = []
        
        for i in range(m):
            new_w = []
            for j in range(n):
                new_w.append(avg(i, j))
                
            new_img.append(new_w)
                
        return new_img
                
        