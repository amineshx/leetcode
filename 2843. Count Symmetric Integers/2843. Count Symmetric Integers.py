class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high+1):
            s=str(num)
            n=len(s)

            if n%2 !=0:
                continue 

            mid = n//2
            left = sum(int(s[i]) for i in range(mid))
            right = sum(int(s[i]) for i in range(mid, n))

            if left == right:
                res+=1
        return res
        