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


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
 
        n = len(nums)
        segment_id = [0] * n
        current_segment = 0
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                current_segment += 1
            segment_id[i] = current_segment
        
        result = []
        for start, end in queries:
            result.append(segment_id[start] == segment_id[end])
        return result