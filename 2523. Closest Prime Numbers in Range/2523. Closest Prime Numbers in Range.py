from typing import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        limit = right + 1
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False 

        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False
        
        primes = [num for num in range(left, right + 1) if is_prime[num]]
        if len(primes) < 2: return [-1, -1]
        
        min_diff = float('inf')
        res = []
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i], primes[i + 1]]

        return res

sol = Solution()
print(sol.closestPrimes(left = 10, right = 19))
print(sol.closestPrimes(left = 4, right = 6))
print(sol.closestPrimes(left = 1, right = 1000000))
print(sol.closestPrimes(left = 19, right = 31))
