from typing import List
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def digit_sum(num):
            div=num
            summ=0
            while div!=0:
                rest=div%10
                summ+=rest
                div//=10
            return summ
        
        digit_sum_map = {}
        res = -1
        
        for num in nums:
            s = digit_sum(num)
            if s in digit_sum_map:
                res = max(res, num + digit_sum_map[s])
                digit_sum_map[s] = max(digit_sum_map[s], num)  
            else:
                digit_sum_map[s] = num  
        
        return res

sol = Solution()
print(sol.maximumSum(nums = [18,43,36,13,7]))
        

