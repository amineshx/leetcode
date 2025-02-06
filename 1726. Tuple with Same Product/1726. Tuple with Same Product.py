from typing import List
from collections import Counter
class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    n=len(nums)
    res = 0
    count = Counter()

    for i in range(n):
      for j in range(i):
        prod = nums[i] * nums[j]
        res += count[prod] * 8
        count[prod] += 1

    return res

sol = Solution()
print(sol.tupleSameProduct(nums = [2,3,4,6]))
print(sol.tupleSameProduct(nums = [1,2,4,5,10]))