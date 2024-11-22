from typing import List
from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)

        for row in matrix:
            row_id = tuple(row)
            if row[0]:
                row_id=tuple([0 if i==1 else 1 for i in row])
            count[row_id]+=1
        
        return max(count.values())

sol =Solution()
print(sol.maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]]))