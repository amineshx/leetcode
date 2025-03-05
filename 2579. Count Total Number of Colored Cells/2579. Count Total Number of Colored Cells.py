# O(n)
class Solution:
    def coloredCells(self, n: int) -> int:
        res=1
        for i in range(1,n):
            res+=i*4
        return res

# O(1)
class Solution:
    def coloredCells(self, n: int) -> int:
        
        return (1+4*((n-1)*n)//2)


sol = Solution()
print(sol.coloredCells(n=1))
print(sol.coloredCells(n=2))
print(sol.coloredCells(n=3))