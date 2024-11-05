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