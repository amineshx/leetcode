# not optimezed solution
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        res= sorted([c for c in range(1, n+1)], key=str)
        return res[k-1]

sol = Solution()
print(sol.findKthNumber(n=13,k=2))