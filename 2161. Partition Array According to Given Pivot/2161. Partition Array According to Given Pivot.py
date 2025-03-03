from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i,i2=0,0
        j=j2=len(nums)-1
        res = [0] * len(nums)

        while j>=0:
            if nums[j] >pivot:
                res[j2]=nums[j]
                j2-=1
            if nums[i]<pivot:
                res[i2]=nums[i]
                i2+=1
            i,j = i+1,j-1
        while i2<=j2:
            res[i2]=res[j2]=pivot
            i2,j2=i2+1,j2-1
        return res