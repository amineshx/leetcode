# sol1 backtracking 
class Solution:
    def minSteps(self, n: int) -> int:
        
        visited={}
        def helper(count,paste):
            if count==n:
                return 0
            if count>n:
                return 1000
            if (count,paste) in visited:
                return visited[(count,paste)]
            
            res1=1+helper(count+paste,paste)
            res2=2+helper(count*2,count)
            visited[(count,paste)]=min(res1,res2)
            return visited[(count,paste)]
        
        if n==1:
            return 0 
        return 1+ helper(1,1)