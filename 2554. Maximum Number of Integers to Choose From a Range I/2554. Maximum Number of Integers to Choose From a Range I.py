from typing import List
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned= set(banned)
        summ=0
        count=0
        i=1
        while summ+i<=maxSum and i <=n:
            if i not in banned:
                summ+=i
                count+=1
            i+=1
        return count


