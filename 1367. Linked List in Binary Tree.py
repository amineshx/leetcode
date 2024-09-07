# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        
        if self.helper(head,root):
            return True
        if not root:
            return False
        return(
            self.isSubPath(head, root.left) or 
            self.isSubPath(head, root.right)
        )
    
    def helper(self,list_node, tree_node):
            if not list_node:
                return True
            if not tree_node or list_node.val!=tree_node.val:
                return False
            return(
                self.helper(list_node.next, tree_node.left) or 
                self.helper(list_node.next, tree_node.right)
            )


def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to create a binary tree from a list
def create_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Create the linked list and binary tree from input
head = create_linked_list([4, 2, 8])
root = create_tree([1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])

# Check if the linked list is a subpath of the binary tree
solution = Solution()
result = solution.isSubPath(head, root)
print(result)  # Output: True or False depending on the result