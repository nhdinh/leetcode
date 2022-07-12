# 119. Pascal's Triangle II
from typing import List


class Solution:
    def getRow(self, rowIndex: int, rows=[[1], [1, 1]]) -> List[int]:
        if rowIndex <= 1:
            return rows[rowIndex]
        else:
            prev_row = self.getRow(rowIndex - 1, rows)
            this_row = [1] * (rowIndex + 1)

            for i in range(1, rowIndex):
                this_row[i] = prev_row[i - 1] + prev_row[i]

            # check
            rows.append(this_row)

            return this_row
