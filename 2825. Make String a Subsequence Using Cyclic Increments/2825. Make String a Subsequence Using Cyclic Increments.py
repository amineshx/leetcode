class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i=j=0
        base=97
        while j<len(str2) and i < len(str1):
            c2 = ord(str2[j])-base
            c1 = ord(str1[i])-base
            if c1 == c2 or (c1+1)%26==c2:
                j+=1
            i+=1
        return j==len(str2)
                

           


