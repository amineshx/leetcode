from typing import List
from math import ceil
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def distribution(x):
            stores = 0
            for quantity in quantities:
                stores+=ceil(quantity/x)
            return stores<=n
        
        left,right=1,max(quantities)
        res = 0
        while left<=right:
            x = left + (right-left)//2
            if distribution(x):
                res = x
                right = x-1
            else:
                left = x+1
        
        return res

sol = Solution()
print(sol.minimizedMaximum(n = 6, quantities = [11,6]))