class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(prefix, n, k):
            if n == 0:
                return prefix
            for c in 'abc':
                if prefix and c == prefix[-1]:
                    continue
                cnt = 2 ** (n2 - len(prefix) - 1)
                if cnt >= k:
                    return dfs(prefix + c, n - 1, k)
                else:
                    k -= cnt
            return ""
        
        n2 = n
        return dfs("", n, k)

sol = Solution()
print(sol.getHappyString(n = 1, k = 3))
print(sol.getHappyString(n = 1, k = 4))
print(sol.getHappyString(n = 3, k = 9))