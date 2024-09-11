class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
       
        differing_bits = start ^ goal
        print(differing_bits)
        # Count the number of 1's in the binary representation of differing_bits
        return bin(differing_bits).count('1')

sol = Solution()
print(sol.minBitFlips(10, 7))
