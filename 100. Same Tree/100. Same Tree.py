from typing import Optional, List
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

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# Test Cases
p1 = build_tree([1,2,3])
q1 = build_tree([1,2,3])

p2 = build_tree([1,2])
q2 = build_tree([1,None,2])

p3 = build_tree([1,2,1])
q3 = build_tree([1,1,2])

solution = Solution()
print(solution.isSameTree(p1, q1))  # True
print(solution.isSameTree(p2, q2))  # False
print(solution.isSameTree(p3, q3)) 