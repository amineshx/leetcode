from typing import List
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


sol = Solution()
print(sol.dividePlayers(skill = [3,2,5,1,3,4]))
