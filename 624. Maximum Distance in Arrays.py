from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins,maxs=[min(sub_array) for sub_array in arrays], [max(sub_array) for sub_array in arrays]
        Min=min(mins)
        Min_index=mins.index(Min)
        Max=max(maxs)
        Max_index=maxs.index(Max)
        if Min_index!=Max_index:
            return Max-Min
        else:
            mins.sort()
            maxs.sort()
            prob=[maxs[-1]-mins[1],maxs[-2]-mins[0]]
            return max(prob)
            
    
sol= Solution()
print(sol.maxDistance(arrays = [[1,2,3],[4,5],[1,2,3]]))