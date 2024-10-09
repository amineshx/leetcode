class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #stack = []
        count = 0
        for c in s :
            if c=='(':
                count+=1
            else :
                count -=1
        return abs(count)