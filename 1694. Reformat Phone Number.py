class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace(" ","").replace("-","")
        
        sufix=""
        n=len(number)
        if n%3==1:
            sufix=number[-4:-2]+"-"+number[-2:]
            n-=4
        elif n%3==2:
            sufix=number[-2:]
            n-=2
        res=""
        for i in range(0,n,3):
            res+=number[i]+number[i+1]+number[i+2]+"-"
        if sufix=="":
            return res[:-1]
        return res+sufix
    

sol=Solution()
print(sol.reformatNumber(number = "123 4-567"))