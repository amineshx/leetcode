from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k  
            remainder_count[remainder] += 1
        print(remainder_count)
        if remainder_count[0] % 2 != 0:
            return False
        for i in range(1, (k // 2) + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False

        return True


sol = Solution()
print(sol.canArrange(arr = [-1,1,-2,2,-3,3,-4,4], k = 3))
        