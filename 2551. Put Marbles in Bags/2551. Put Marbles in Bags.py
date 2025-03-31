from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights)==k or k==1:
            return 0
        
        sums=[]
        for i in range(len(weights)-1):
            sums.append(weights[i]+weights[i+1])
        
        sums.sort()
        min_score = sum(sums[:k-1])
        max_score = sum(sums[-(k-1):])
        

        return max_score-min_score
    
sol = Solution()
print(sol.putMarbles(weights = [1,3,5,1], k = 2)) # 4
        
