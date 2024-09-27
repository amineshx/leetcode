class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        resultArr = 0
        j = 0
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            
            while product >= k and j <= i:
                product /= nums[j]
                j += 1
            
            resultArr += i - j +1
        
        return resultArr
