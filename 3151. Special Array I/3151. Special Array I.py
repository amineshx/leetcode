from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        for i in range(len(nums)-1):
            if nums[i]%2==0:
                if nums[i+1]%2!=1:
                    return False
            else:
                if nums[i+1]%2!=0:
                    return False
        return True

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            if nums[i] & 1 == nums[i-1]&1:
                return False
        return True
sol = Solution()
print(sol.isArraySpecial(nums = [2,1,4]))