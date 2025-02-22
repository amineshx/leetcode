# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dash_num = 0
        stack = []
        i=0

        while i<len(traversal):
            if traversal[i]=='-':
                dash_num+=1
                i+=1
            else:
                j=i
                while j< len(traversal) and traversal[j]!='-':
                    j+=1
                val = int(traversal[i:j])
                node = TreeNode(val)

                while len(stack)>dash_num:
                    stack.pop()
                
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)
                i=j
                dash_num=0
        return stack[0]

sol = Solution()
print(sol.recoverFromPreorder(traversal = "1-2--3--4-5--6--7"))
print(sol.recoverFromPreorder(traversal = "1-2--3---4-5--6---7"))
print(sol.recoverFromPreorder(traversal = "1-401--349---90--88"))