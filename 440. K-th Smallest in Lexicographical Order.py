# not optimezed solution

class Solution:
    def helper(self,current,n):
        res=0
        nei=current+1
        while current <= n:
            res+=min(nei,n+1)-current
            current*=10
            nei*=10
        return res
    def findKthNumber(self, n: int, k: int) -> int:
        current=1
        i=1

        while i<k:
            steps=self.helper(current,n)
            if i +steps <=k:
                current+=1
                i+=steps
            else :
                current*=10
                i+=1
        return current

sol = Solution()
print(sol.findKthNumber(n=13,k=2))