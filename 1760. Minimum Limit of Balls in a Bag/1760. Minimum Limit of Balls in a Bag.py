from typing import List
from math import ceil
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def isDividable(number):
            operations = 0
            for num in nums:
                operations += ceil(num/number) -1
                if operations > maxOperations:
                    return False
            return True
        
        left, right = 1, max(nums)
        while left<right:
            mid = left + ((right-left)//2)
            if isDividable(mid):
                right = mid
            else:
                left = mid+1
        return left

