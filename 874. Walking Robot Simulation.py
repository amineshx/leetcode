from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions= [[0,1],[1,0],[0,-1],[-1,0]]
        x,y,dist,res=0,0,0,0
        obstacles = {tuple(obst) for obst in obstacles}

        for command in commands:
            if command==-1:
                dist = (dist+1)%4
            elif command==-2:
                dist = (dist-1)%4
            else:
                DeltaX , DeltaY = directions[dist]
                for _ in range(command):
                    position = (x+DeltaX , y+DeltaY)
                    if position in obstacles :
                        break
                    x,y= x+DeltaX , y+DeltaY
            res = max(res, x**2 + y**2)
        return res



