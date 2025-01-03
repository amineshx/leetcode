from typing import List

'''
could be a solution but not efficient , and need some fixes
'''
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [[0,0] for _ in range(len(nums))]
        print(prefix)
        res = 0
        left_sum,right_sum=0,0
        for i, num in enumerate(nums):
            left_sum=prefix[i][0]+num
            right_sum=0
            for num2 in range(i+1,len(nums)):
                right_sum += right_sum+num2
            prefix[i][0]=left_sum
            prefix[i][1]=right_sum
        

        
        return prefix

sol = Solution()
print(sol.waysToSplitArray(nums = [10,4,-8,7]))




'''
efficient but didn't pass all test cases
'''

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_arr = sum(nums)
        res = 0
        for i in range(len(nums)):
            sum_arr-=nums[i] 
            if sum_arr <= nums[i] and i != len(nums)-1:
                res+=1
        return res

sol = Solution()
print(sol.waysToSplitArray(nums = [10,4,-8,7]))


'''
fixed solution
'''

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_arr = sum(nums)
        left_sum = 0
        res = 0
        
        for i in range(len(nums) - 1):  
            left_sum += nums[i]
            right_sum = sum_arr - left_sum
            if left_sum >= right_sum:
                res += 1
                
        return res

sol = Solution()
print(sol.waysToSplitArray(nums = [10,4,-8,7]))

