from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: 
            return 0
        left=1
        right= max(candies)
        res = 0

        while left<=right:
            mid=(left+right)//2
            child_cnt = sum(c // mid for c in candies)

            if child_cnt>=k:
                res=mid
                left=mid+1
            else:
                right=mid-1
        
        return res