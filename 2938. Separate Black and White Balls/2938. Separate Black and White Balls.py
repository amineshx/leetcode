#this sol doesn't work

class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)-1
        i=n
        res=0
        while i >=0 :
            print("i: ",i)
            if s[i]=='1':
                if i==n:
                    i-=1
                print("if s[i]=='1':")
                j=i
                print("j: ",j)
                while j<n:
                    temp=s[j]
                    s[j]=s[j+1]
                    s[j+1]=temp
                    res+=1
                    j+=1
                    print(s)
                    print("res", res)
                    print("j: ",j)
            else:
                i-=1
        return res

# this sol doesn't work
class Solution:
    def minimumSteps(self, s: str) -> int:
        n=len(s)
        white_count=0
        swaps=0

        for i in range(n):
            if s[i]=='0':
                white_count+=1
            else:
                swaps+=white_count
        return swaps
    
sol = Solution()
print(sol.minimumSteps("101"))


        
