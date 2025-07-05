from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_map = {}
        for ele in arr:
            if ele in freq_map:
                freq_map[ele]+=1
            else:
                freq_map[ele]=1
        
        maxi = 1
        found=False
        for ele in freq_map:
            if ele == freq_map[ele]:
                found=True
                maxi=max(maxi,freq_map[ele])
        if not found:
            return -1
        return freq_map.get(maxi)

sol = Solution()
print(sol.findLucky([2,2,4]))