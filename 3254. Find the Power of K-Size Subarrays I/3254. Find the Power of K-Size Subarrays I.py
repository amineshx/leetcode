from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        right = k-1
        
        while right <len(nums):
            check = True
            for i in range(left,right):
                if nums[i]>nums[i+1] or nums[i+1]-nums[i]!=1:
                    res.append(-1)
                    check=False
                    break
            if check:
                res.append(nums[right])
            right+=1
            left+=1
        return res

sol = Solution(nums = [1,2,3,4,3,2,5], k = 3)
