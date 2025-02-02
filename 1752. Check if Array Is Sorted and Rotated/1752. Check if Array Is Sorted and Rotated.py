from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        window_length = 1

        for i in range(1,2*n):
            if nums[(i-1)%n] <=nums[i%n]:
                window_length+=1

            else: window_length=1

            if window_length==n:return True
        
        return n==1

sol = Solution()
print(sol.check(nums = [3,4,5,1,2]))
print(sol.check(nums = [2,1,3,4]))
print(sol.check(nums = [1,2,3]))