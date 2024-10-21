class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def DFS(i, current_set):
            if i==len(s):
                return 0
        
            res = 0
            for j in range(i,len(s)):
                substr = s[i:j+1]
                if substr in current_set:
                    continue

                current_set.add(substr)
                res = max(res,1+DFS(j+1, current_set))
                current_set.remove(substr)
            return res 
        
        return DFS(0,set())
        
    