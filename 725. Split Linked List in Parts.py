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
        
        sub_length , remainder = length // k , length%k
        cur = head
        res = []
        for _ in range(k):
            res.append(cur)
            loop_range = sub_length-1 + (1 if remainder else 0)
            for __ in range(loop_range):
                if not cur:
                    break
                cur=cur.next

            remainder-=(1 if remainder else 0)
            if cur:
                cur.next , cur = None,cur.next

        return res


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


# Create the linked list and binary tree from input
head = create_linked_list([1,2,3])
k = 5

# Use the Solution class to split the list
solution = Solution()
result = solution.splitListToParts(head,k)
print([linked_list_to_list(part) for part in result])