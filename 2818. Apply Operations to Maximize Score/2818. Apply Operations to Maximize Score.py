from typing import List
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        N = max(nums) + 1  
        
        prime_scores = [0] * N
        for i in range(2, N):
            if prime_scores[i] == 0:  
                for j in range(i, N, i):
                    prime_scores[j] += 1
        
        n = len(nums)
        left, right = [0] * n, [0] * n
        stack = []

        for i in range(n):
            while stack and prime_scores[nums[stack[-1]]] < prime_scores[nums[i]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and prime_scores[nums[stack[-1]]] <= prime_scores[nums[i]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        contrib = []
        for i in range(n):
            l_range = i - left[i]
            r_range = right[i] - i
            contrib.append((nums[i], l_range * r_range))  

        contrib.sort(reverse=True, key=lambda x: x[0])

        res, used = 1, 0
        for value, count in contrib:
            times = min(k - used, count)
            res = (res * pow(value, times, mod)) % mod  
            used += times
            if used == k:
                break

        return res


sol = Solution()
print(sol.maximumScore(nums = [8,3,9,3,8], k = 2))
print(sol.maximumScore(nums = [19,12,14,6,10,18], k = 3))



