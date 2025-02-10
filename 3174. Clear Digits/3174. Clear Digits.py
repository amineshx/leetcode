class Solution:
    def clearDigits(self, s: str) -> str:
        res=[]

        for char in s:
            
            print("char",char," res",res)
            if (ord(char)>122 or ord(char)<97) and res:
                res.pop()
                continue
            res.append(char)
                
                
        return ''.join(res)

sol = Solution()
print(sol.clearDigits(s="fdd14"))
print(sol.clearDigits(s= "abc"))
print(sol.clearDigits(s = "cb34"))