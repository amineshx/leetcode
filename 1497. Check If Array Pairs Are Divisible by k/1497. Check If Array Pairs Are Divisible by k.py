from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [((x%k)+k)%k for x in arr]
        n=len(arr)
        left = 0
        right = n-1
        while left < right:
            if freq[left]+freq[right]%k ==0:
                if right-left==1 and freq[right]+freq[left]!=0:
                    return False
            left+=1
            right-=1
                
        return True

sol = Solution()
print(sol.canArrange(arr = [-1,1,-2,2,-3,3,-4,4], k = 3))
        