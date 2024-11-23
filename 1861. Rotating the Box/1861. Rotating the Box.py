from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        res=[]
        m,n=len(box),len(box[0])

        for row in box:
            i=n-1
            for j in reversed(range(n)):
                if row[j]=="#":
                    row[j],row[i]=row[i],row[j]
                    i-=1
                elif row[j]=="*":
                    i=j-1

        for c in range(n):
            col = []
            for r in reversed(range(m)):
                col.append(box[r][c])
            res.append(col)
        return res
        

                    
                        


sol = Solution()
print(sol.rotateTheBox(box = [["#",".","*","."],
              ["#","#","*","."]]))