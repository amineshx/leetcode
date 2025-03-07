from typing import List
import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        primes = [num for num in range(left, right + 1) if is_prime(num)]
        if len(primes) < 2: return [-1, -1]
        
        min_diff = float('inf')
        res = []
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i], primes[i + 1]]

        return res