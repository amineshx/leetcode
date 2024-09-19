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