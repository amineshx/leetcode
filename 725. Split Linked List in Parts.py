from typing import Optional,List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length,cur = 0,head

        # getting the length of the linkdlist
        while cur:
            cur=cur.next
            length+=1
        