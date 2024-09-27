# Definition for singly-linked list.
from typing import Optional,List
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


def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


head = create_linked_list([18,6,10,3])
solution = Solution()
result = solution.insertGreatestCommonDivisors(head)
print(linked_list_to_list(result))