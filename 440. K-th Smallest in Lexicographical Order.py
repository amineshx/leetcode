# not optimezed solution
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        res = []
        for i, c in enumerate(sorted(range(1, n+1), key=str), start=1):
            res.append(c)
            if i == k:
                return c

sol = Solution()
print(sol.findKthNumber(n=13,k=2))