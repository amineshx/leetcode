from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0
        odd_count = 0 
        even_count = 0
        res = 0
        mod = 10**9 + 7 

        for num in arr:
            prefix_sum+=num 

            if prefix_sum%2:
                res += 1+even_count
                odd_count+=1
            else:
                res+= odd_count
                even_count+=1
        return res % mod