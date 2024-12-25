# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            row_max = q[0].val
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                row_max = max(row_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
            res.append(row_max)
        return res


''' just to excute the code'''

# Function to build a tree from a level-order list
def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    q = deque([root])
    i = 1
    while q and i < len(level_order):
        node = q.popleft()
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            q.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            q.append(node.right)
        i += 1
    return root

# Example input
level_order = [1, 3, 2, 5, 3, None, 9]

# Build the tree and execute the solution
root = build_tree(level_order)
solution = Solution()
result = solution.largestValues(root)

# Print the result
print(result)