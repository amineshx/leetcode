from typing import List
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        max_len = -1
        num_set = set(nums)
        sorted_nums = sorted(num_set)
    
        for num in sorted_nums:
            count = 0
            curr = num
            while curr in num_set:
                num_set.remove(curr)
                curr = curr ** 2
                count += 1
            
            max_len = max(max_len, count)
        
        return max_len if max_len > 1 else -1