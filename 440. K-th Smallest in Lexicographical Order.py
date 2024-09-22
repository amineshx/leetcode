# not optimezed solution
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        count = 0
        for c in sorted(range(1, n + 1), key=str):
            count += 1
            if count == k:
                return c

sol = Solution()
print(sol.findKthNumber(n=13,k=2))