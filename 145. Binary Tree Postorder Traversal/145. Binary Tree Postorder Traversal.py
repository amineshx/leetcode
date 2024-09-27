# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[root]
        visited=[False]
        res=[]

        while stack:
            cur,v=stack.pop(), visited.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


sol = Solution()
print(sol.postorderTraversal(root)) 