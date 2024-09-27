# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for i, l in enumerate(lists):
            current = l
            while current:
                res.append(current.val)
                current = current.next
        
        res.sort()
        dummy = ListNode(0)
        current = dummy
        for val in res:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next



# this code has no relation to the challenge just so i can build the linklist



def build_linked_list(arr):
    if not arr:  
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Convert the input lists to a list of ListNode objects
lists = [
    build_linked_list([1, 4, 5]),
    build_linked_list([1, 3, 4]),
    build_linked_list([2, 6])
]

def print_linked_list(node: Optional[ListNode]):
    current = node
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create an instance of the solution and call the method
sol = Solution()
merged_list = sol.mergeKLists(lists)

# Print the merged linked list
print_linked_list(merged_list)
