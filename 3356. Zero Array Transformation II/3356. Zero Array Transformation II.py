from typing import List

# brute force way O(n*m)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0
        m=len(queries)

        def check_if_zero():
            return all(num == 0 for num in nums)  
        
        for i in range(m):
            l, r, val = queries[i]
            
            for j in range(l, r + 1):
                nums[j] = max(0, nums[j] - val)
            
            if check_if_zero():
                return i + 1  
        
        return -1  
