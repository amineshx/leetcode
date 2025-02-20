from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strings_set = { num for num in nums}
        def backtracking(i, current):
            if i == len(nums):
                res = "".join(current)
                return None if res in strings_set else res 
            
            res = backtracking(i+1, current)
            if res: 
                return res
            
            current[i]='1'
            res = backtracking(i+1, current)
            if res:
                return res
        
        return backtracking(0,["0" for _ in nums])

sol = Solution()
print(sol.findDifferentBinaryString(nums = ["01","10"]))
print(sol.findDifferentBinaryString(nums = ["00","01"]))
print(sol.findDifferentBinaryString(nums = ["111","011","001"]))