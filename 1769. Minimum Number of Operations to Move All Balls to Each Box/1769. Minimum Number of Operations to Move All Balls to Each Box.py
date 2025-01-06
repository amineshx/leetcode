from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0]*len(boxes)

        balles, moves = 0,0

        for i in range(len(boxes)):
            res[i]+=balles+moves
            moves+=balles
            balles+=int(boxes[i])
        
        balles, moves = 0,0
        for i in reversed(range(len(boxes))):
            res[i]+=balles+moves
            moves+=balles
            balles+=int(boxes[i])
        
        return res

sol = Solution()
print(sol.minOperations(boxes = "001011"))