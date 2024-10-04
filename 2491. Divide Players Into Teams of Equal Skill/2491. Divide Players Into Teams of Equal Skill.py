from typing import List
from collections import Counter

# sol1
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        
        skill.sort()
        n=len(skill)
        target = skill[0]+skill[n-1]
        res = skill[0]*skill[n-1]
        
        left,right=1,n-2
        while left<right:
            summ = skill[left]+skill[right]
            if summ != target:
                return -1
            else :
                res+= skill[left]*skill[right]
            
            left+=1
            right-=1
        return res


#sol2
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)

        if (2*total) % len(skill):
            return -1
        
        count = Counter(skill)
        target = (2*total) // len(skill)
        res = 0

        for s in skill :
            if not count[s]:
                continue
            diff = target - s
            if not count[diff]:
                return -1

            res += s*diff
            count[s]-=1
            count[diff]-=1    
        return res

sol = Solution()
print(sol.dividePlayers(skill = [3,2,5,1,3,4]))
