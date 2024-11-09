class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res=x
        xi=1
        ni=1

        while ni <=n-1:
            if xi & x ==0:
                if ni & (n-1):
                    res = res | xi
                
                ni = ni << 1
            
            xi = xi << 1

        return res  