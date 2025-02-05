from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count_diff=0
        n=len(s1)
        if Counter(s1) != Counter(s2):
            return False 
        for i in range(n):
            if s1[i]!=s2[i]:
                count_diff+=1
        
        if count_diff>2 or count_diff==1 :
            return False

        return True

sol = Solution()
print(sol.areAlmostEqual(s1 = "bank", s2 = "kanb"))
print(sol.areAlmostEqual(s1 = "attack", s2 = "defend"))
print(sol.areAlmostEqual(s1 = "kelb", s2 = "kelb"))