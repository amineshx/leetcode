from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!= len(original):
            return []
        
        res=[]
        for i in range(m):
            start_pointer = i*n
            end_pointer = start_pointer + n
            res.append(original[start_pointer:end_pointer])
        
        return res 

