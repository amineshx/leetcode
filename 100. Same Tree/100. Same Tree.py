from typing import Optional
from collections import deque  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque([p])  
        queue_q = deque([q])  
        while queue_p and queue_q:
            node_p = queue_p.popleft()
            node_q = queue_q.popleft()
            if not node_p and not node_q:
                continue
            if not node_p or not node_q or node_q.val!=node_p.val:
                return False
            
            queue_p.append(node_p.left)
            queue_q.append(node_q.left)
            queue_p.append(node_p.right)
            queue_q.append(node_q.right)

        return not queue_p and not queue_q