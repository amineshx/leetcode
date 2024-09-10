# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur.next:
            node1,node2 = cur.val, cur.next.val
            cur.next=ListNode(self.GCD(node1,node2),cur.next)
            cur=cur.next.next
        return head
    
    
    def GCD(self,a,b):
        while b>0:
            a,b=b,a%b
        return a