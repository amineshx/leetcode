class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=''
        print('res: ',res)
        print('-----------before-------')
        for c in s:
            cToADD=str(ord(c)-96)
            res+=cToADD
            print('res: ',res)
        print('-----------after-------')
        while k>=1:
            newRes=0
            for c in res:
                newRes+=int(c)
            k-=1
            res=str(newRes)
        
        return newRes

sol = Solution()
print(sol.getLucky(s = "leetcode", k = 2))