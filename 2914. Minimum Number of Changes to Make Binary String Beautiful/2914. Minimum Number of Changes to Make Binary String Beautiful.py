#sol1

class Solution:
    def minChanges(self, s: str) -> int:
        left = 0
        res=0

        for right in range(len(s)):
            if s[left]!=s[right]:
                if right%2==0:
                    res+=1
                left = right
        return res 
    
#sol2
class Solution:
    def minChanges(self, s: str) -> int:
        res=0
        for pointer in range(0,len(s),2):
            if s[pointer]!=s[pointer+1]:
                res+=1
        return res 
                