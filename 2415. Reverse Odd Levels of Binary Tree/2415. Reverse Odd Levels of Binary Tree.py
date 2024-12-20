# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        i=0
        while q:
            if i % 2==1:
                l,r=0,len(q)-1
                while l<r:
                    q[l].val,q[r].val=q[r].val,q[l].val
                    l+=1
                    r-=1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i+=1
        return root


# Helper function to construct a binary tree from a list
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root



''' 
    just to execute the code 
'''

# Helper function to print the tree level order (for testing)
def print_tree(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for a cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Input list
values = [2, 3, 5, 8, 13, 21, 34]

# Build the tree
root = build_tree(values)

# Solution
sol = Solution()
result_root = sol.reverseOddLevels(root)

# Print the result tree
print(print_tree(result_root))
