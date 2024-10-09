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

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_parentesis = 0
        res = 0

        for c in s:
            if c =="(":
                open_parentesis +=1
            else :
                if open_parentesis==0:
                    res+=1
                open_parentesis = max(open_parentesis-1,0)
        return res + open_parentesis