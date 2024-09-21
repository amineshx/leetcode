from typing import List 
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted([c for c in range(1, n+1)], key=str)

       
