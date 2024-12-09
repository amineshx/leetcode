from typing import List

# brut force approch
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums)==1:
                return True
        
        def isIntervalSpecial(start, end):
            
            for i in range(start,end):
                if nums[i]%2==0:
                    if nums[i+1]%2!=1:
                        return False
                else:
                    if nums[i+1]%2!=0:
                        return False
            return True
        res = []
        for querie in queries:
            start,end = querie[0], querie[1]
            res.append(isIntervalSpecial(start,end))
        
        return res
