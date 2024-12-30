class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        modulo = 10**9 + 7
        memo = {}

        def dfs(length):
            if length > high:
                return 0
            
            if length in memo:
                return memo[length]
            
            memo[length] = 1 if length >= low else 0
            memo[length] += dfs(length + zero) + dfs(length + one)

            return memo[length] % modulo
        
        return dfs(0)

sol = Solution()
print(sol.countGoodStrings(low = 3, high = 3, zero = 1, one = 1))