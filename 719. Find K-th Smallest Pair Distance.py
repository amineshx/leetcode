from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right=0,nums[-1]

        def count_num_pairs(diff):
            i=0
            res=0
            for j in range(len(nums)):
                while nums[j]-nums[i]>diff:
                    i+=1
                res+=j-i
            return res
        while left<right:
            mid= (left+right)//2
            pairs= count_num_pairs(mid)
            if pairs >=k:
                right=mid
            else:
                left=mid+1
        
        return left