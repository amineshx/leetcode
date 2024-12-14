from typing import List
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        n = len(nums)
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))

        for num, index in sorted_nums:
            if nums[index]!=-1:
                score+=num
                nums[index]=-1
                if index>0:
                    nums[index-1]=-1
                if index<n-1:
                    nums[index+1]=-1
        return score
