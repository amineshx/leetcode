from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        while len(nums) != len(set(nums)):
            print(f"nums {nums}")
            print(f"setnums {set(nums)}")
            nums = nums[3:]
            operations += 1
        return operations



sol = Solution()
print(sol.minimumOperations(nums = [1,2,3,4,2,3,3,5,7]))
