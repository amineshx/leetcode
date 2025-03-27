from typing import List
from collections import defaultdict, Counter

# O(n) sol
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = Counter(nums)

        for i in range(len(nums)):
            left[nums[i]]+=1
            right[nums[i]]-=1

            left_len = i+1
            right_len = len(nums) -i -1

            if 2* left[nums[i]]>left_len and 2*right[nums[i]]>right_len:
                return i 
        return -1
    

# voting solution 
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = 0
        majority = 0

        for num in nums:
            if count==0:
                majority=num
                count=1
            elif num==majority:
                count+=1
            else: count-=1
            
        left_count = 0
        right_count = nums.count(majority)

        for i in range(len(nums)):
            if nums[i] == majority:

                left_count+=1
                right_count-=1

            left_len = i+1
            right_len = len(nums) -i -1

            if 2* left_count>left_len and 2*right_count>right_len:
                return i 
        return -1