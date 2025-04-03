from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    op = (nums[i]-nums[j])*nums[k]
                    res = max(op,res)
        return res


sol = Solution()
print(sol.maximumTripletValue(nums = [12,6,1,2,7]))
print(sol.maximumTripletValue(nums = [1,10,3,4,19]))
print(sol.maximumTripletValue(nums = [1,2,3]))