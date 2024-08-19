# sol1 backtracking 
# class Solution:
#     def minSteps(self, n: int) -> int:
        
#         visited={}
#         def helper(count,paste):
#             if count==n:
#                 return 0
#             if count>n:
#                 return 1000
#             if (count,paste) in visited:
#                 return visited[(count,paste)]
            
#             res1=1+helper(count+paste,paste)
#             res2=2+helper(count*2,count)
#             visited[(count,paste)]=min(res1,res2)
#             return visited[(count,paste)]
        
#         if n==1:
#             return 0 
#         return 1+ helper(1,1)


class Solution:
    def minSteps(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=0

        for i in range(2,n+1):
            for j in range(1,1+(i//2)):
                if i%j==0:
                    dp[i]=min(dp[i],dp[j]+i//j)
        
        return dp[n]