from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res_len = [0]*32
        res = float("inf")
        
        def update_res_len(res_len,num, diff):
            for i in range(32):
                if num & (1<<i):
                    res_len[i]+=diff
        
        def arr_to_int(res_len):
            res = 0
            for i in range(32):
                if res_len[i]:
                    res+=(1 << i)
            return res

        left=0
        for right in range(len(nums)):
            update_res_len(res_len, nums[right], 1)
            current_or = arr_to_int(res_len)
            while left <= right and current_or >=k:
                res = min(res, right-left+1)
                update_res_len(res_len, nums[left], -1)
                current_or = arr_to_int(res_len)
                left+=1
        return -1 if res==float("inf") else res
            
sol = Solution()
print(sol.minimumSubarrayLength(nums = [1,2,3], k = 2))
