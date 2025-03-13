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
    
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)

        left, right = 0, m
        result = -1

        while left <= right:
            mid = (left + right) // 2
            diff = [0] * (n + 1)
            for i in range(mid):
                li, ri, vali = queries[i]
                diff[li] -= vali
                if ri + 1 < n:
                    diff[ri + 1] += vali

            applied = 0
            zero_array = True

            for i in range(n):
                applied += diff[i]
                if nums[i] + applied > 0:
                    zero_array = False
                    break
            
            if zero_array:
                result = mid  
                right = mid - 1  
            else:
                left = mid + 1  
            
        return result
