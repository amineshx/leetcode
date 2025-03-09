from typing import List
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        res=0

        for i in range(n):
            check=True

            for j in range(1,k):
                if colors[(i+j)%n]==colors[(i+j-1)%n]:
                    check=False
                    break
            if check:
                res+=1
        
        return res