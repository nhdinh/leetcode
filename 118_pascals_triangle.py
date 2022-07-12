# 118. Pascal's Triangle

from typing import List


class Solution:
    # pascal triangle
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return 0
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            prev_triangle = self.generate(numRows - 1)
            prev_row = prev_triangle[numRows - 2]
            this_row = [1] * numRows
            
            for i in range(1, numRows - 1):
                this_row[i] = prev_row[i - 1] + prev_row[i]  
                
            prev_triangle.append(this_row)
            return prev_triangle