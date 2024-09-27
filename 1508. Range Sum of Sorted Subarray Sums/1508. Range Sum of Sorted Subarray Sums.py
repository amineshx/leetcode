from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarr_sum=[]
        MOD=10**9 + 7

        for i in range(n):
            cur_sum=0
            for j in range(i,n):
                cur_sum=(cur_sum+nums[j])%MOD
                subarr_sum.append(cur_sum)
        subarr_sum.sort()
        res=0
        for i in range(left-1,right):
            res=(res+subarr_sum[i])%MOD
        return res

num=Solution()
print(num.rangeSum([1,2,3,4], 4, 1,  5))