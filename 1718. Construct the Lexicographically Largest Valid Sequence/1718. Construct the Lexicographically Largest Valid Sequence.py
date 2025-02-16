from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        res = [0]*(2*n-1)
        placed = set()

        def backtrack(i):
            if i==len(res):
                return True
            for num in reversed(range(1, n+1)):
                if num in placed:
                    continue
                if num>1 and (i+num>= len(res) or res[i+num]):
                    continue
                placed.add(num)
                res[i]=num
                if num>1:
                    res[i+num]=num
                j=i+1
                while j<len(res) and res[j]:
                    j+=1
                if backtrack(j):
                    return True
                
                placed.remove(num)
                res[i]=0
                if num>1:
                    res[i+num]=0
            return False

        backtrack(0)
        return res

sol = Solution()
print(sol.constructDistancedSequence(n=3))
print(sol.constructDistancedSequence(n=5))