# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
#         left,right,top,bottom = 0,n,0,m 
#         res = [[-1]*n for _ in range(m)]

#         while head :
#             for i in range(left,right):
#                 if not head :
#                     return res
#                 res[top][i]=head.val
#                 head = head.next
#             top+=1

#             for i in range(top,bottom):
#                 if not head :
#                     return res
#                 res[i][right-1]=head.val
#                 head = head.next
#             right-=1

#             for i in range(right-1,left-1,-1):
#                 if not head :
#                     return res
#                 res[bottom-1][i]=head.val
#                 head = head.next
#             bottom-=1

#             for i in range(bottom-1,top-1,-1):
#                 if not head :
#                     return res
#                 res[i][left]=head.val
#                 head = head.next
#             left+=1
        
#         return res


#sol 2
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left,right,top,bottom = 0,n,0,m 
        res = [[-1]*n for _ in range(m)]

        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        row,col,direction = 0,0,0

        while head :
            dirR , dirC = directions[direction]
            
            while(head and left <= col <right and top <= row < bottom and res[row][col]==-1):
                res[row][col] = head.val
                head = head.next
                row,col = row+dirR , col+dirC
            row,col = row-dirR , col-dirC
            direction = (direction+1)%4
            dirR , dirC = directions[direction]
            row,col = row+dirR , col+dirC
        return res