from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        i=0
        while i < k:
            min_num = min(nums)
            idx = nums.index(min_num)
            nums[idx]=min_num*multiplier
            i+=1
        return nums

sol = Solution()
print(sol.getFinalState( nums = [2,1,3,5,6], k = 5, multiplier = 2))


