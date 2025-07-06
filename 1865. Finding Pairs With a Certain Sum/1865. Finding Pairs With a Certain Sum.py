from typing import List
from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2 
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val+val
        self.freq[old_val]-=1
        if self.freq[old_val]==0:
            del self.freq[old_val]
        self.freq[new_val]+=1
        self.nums2[index]=new_val


    def count(self, tot: int) -> int:
        res=0
        for num in self.nums1:
            complement = tot-num
            res+=self.freq.get(complement,0)
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)