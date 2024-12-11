class Solution:
    def maximumLength(self, s: str) -> int:

        n = len(s)
        left,right=1, n 
        if not self.helper(s,n,left):
            return -1
        while left+1<right:
            mid = left + (right-left)//2
            if self.helper(s,n,mid):
                left=mid
            else:
                right=mid
        return left
    
    def helper(self,s: str, n:int, x:int )-> bool:
        count = [0]*26
        p = 0
        for i in range(n):
            while s[p]!=s[i]:
                p+=1
            if i-p+1>=x:
                count[ord(s[i])-ord('a')]+=1
            if count[ord(s[i])-ord('a')]>2:
                return True
        return False