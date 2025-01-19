from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftBlock = rightBlock = 0
        maxLeft = [0]*n
        maxRight = [0]*n
        output = 0
        for i in range(n):
            j= -i-1
            maxLeft[i]=leftBlock
            maxRight[j]=rightBlock
            leftBlock = max(leftBlock, height[i])
            rightBlock = max(rightBlock,height[j])
        for i in range(n):
            currentPosition = min(maxLeft[i],maxRight[i]) - height[i]
            if currentPosition>0:
                output +=currentPosition
        return output

