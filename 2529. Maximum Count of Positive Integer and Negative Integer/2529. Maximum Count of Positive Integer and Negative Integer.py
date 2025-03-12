from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        count_neg = 0
        count_zero = 0

        for i in range(n):
            if nums[i]<0:
                count_neg+=1
            elif nums[i]==0:
                count_zero+=1
            else:break
        return max(n-count_zero-count_neg,count_neg)

sol = Solution()
print(sol.maximumCount(nums = [-2,-1,-1,1,2,3]))
print(sol.maximumCount(nums = [-3,-2,-1,0,0,1,2]))
print(sol.maximumCount(nums = [5,20,66,1314]))