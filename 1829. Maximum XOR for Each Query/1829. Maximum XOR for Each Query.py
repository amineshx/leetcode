from typing import List 
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res =0 
        for num in nums:
            res^=num
        
        mask = (1<< maximumBit)-1
        answer = []
        for num in reversed(nums):
            answer.append(res^mask)
            res^=num
        
        return answer