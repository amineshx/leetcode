from typing import List
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x=0
        for n in derived:
            if n:
                x=~x
        
        return 0==x

sol = Solution()
print(sol.doesValidArrayExist(derived = [1,1,0]))