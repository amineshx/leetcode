from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        remaining = k % total

        for i,c in enumerate(chalk):
            if remaining < c :
                return i
            remaining -= c
        return 0
        

sol =Solution()
print(sol.chalkReplacer(chalk=[5,1,5], k=22))