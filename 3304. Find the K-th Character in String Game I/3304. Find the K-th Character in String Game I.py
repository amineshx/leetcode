from string import ascii_lowercase
class Solution:
    def kthCharacter(self, k: int) -> str:
        return ascii_lowercase[(k-1).bit_count()]

sol = Solution()
print(sol.kthCharacter(k=5))
print(sol.kthCharacter(k=10))