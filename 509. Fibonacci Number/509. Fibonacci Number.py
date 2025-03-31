# tabulation
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        nums = [0]*(n+1)
        nums[1]=1
        for i in range(n):  
            if i + 1 < len(nums):
                nums[i + 1] += nums[i]
            if i + 2 < len(nums):  
                nums[i + 2] += nums[i]
        return nums[n]
    
# memo
class Solution:
    def fib(self, n: int) -> int:
        def calc(n,memo):
            if n==0:return 0
            if n<=2:return 1
            if n in memo : return memo[n]
            memo[n]=calc(n-1,memo)+calc(n-2,memo)
            return memo[n]
        return calc(n,memo={})


sol = Solution()
print(sol.fib(n=2))
print(sol.fib(n=3))
print(sol.fib(n=4))