from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {}
        for idx,char in enumerate(s):
            last_occ[char]=idx 
        
        max_last = 0
        res = []
        count=0
        for i,c in enumerate(s):
            if max_last < last_occ[c]:
                max_last=last_occ[c]    
            count+=1
            if i==max_last:
                res.append(count)
                count=0
        return res
    
sol = Solution()
print(sol.partitionLabels(s = "ababcbacadefegdehijhklij"))
print(sol.partitionLabels(s = "eccbbbbdec"))