from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def count_the_prime_score(x):
            count=0
            dub = set()
            i=2
            while x>1:
                if x%i==0:
                    x=x//i
                    if i not in dub:
                        dub.add(i)
                        count+=1
                else:i+=1
            return count
        mod = 10**9+7
        res = 1
        prime_scores = {}
        for num in nums:
            if num not in prime_scores:
                prime_scores[num]=count_the_prime_score(num)

        new_nums = [(prime_scores[value],index,value) for index,value in enumerate(nums)]
        new_nums.sort(key=lambda x: (-x[0], x[1]))

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
            for _ in range(times):
                res = (res * value) % mod
            used += times
            if used == k:
                break

        return res

sol = Solution()
print(sol.maximumScore(nums = [8,3,9,3,8], k = 2))



