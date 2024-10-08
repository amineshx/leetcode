from typing import List
class Solution:

    operations = {
        "+": lambda x,y:x+y,
        "-": lambda x,y:x-y,
        "*": lambda x,y:x*y,
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.expression=expression
        return self.BackTracking(0,len(self.expression)-1)
    



    def BackTracking(self,left,right):
        res=[]

        for i in range(left,right+1):
            op = self.expression[i]
            if op in Solution.operations:
                nums1=self.BackTracking(left,i-1)
                nums2=self.BackTracking(i+1,right)

                for n1 in nums1:
                    for n2 in nums2:
                        res.append(Solution.operations[op](n1,n2))
        if res==[]:
            res.append(int(self.expression[left:right+1]))
        return res

class Solution:
    operations = {
        "+": lambda x,y:x+y,
        "-": lambda x,y:x-y,
        "*": lambda x,y:x*y,
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        res=[]

        for i in range(len(expression)):
            op = expression[i]
            if op in self.operations:
                nums1=self.diffWaysToCompute(expression[:i])
                nums2=self.diffWaysToCompute(expression[i+1:])

                for n1 in nums1:
                    for n2 in nums2:
                        res.append(self.operations[op](n1,n2))
        if res==[]:
            res.append(int(expression))
        return res

sol = Solution()
print(sol.diffWaysToCompute("2-1-1"))
        
    