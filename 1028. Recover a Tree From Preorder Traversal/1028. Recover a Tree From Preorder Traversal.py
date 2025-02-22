from typing import Optional,List
from collections import deque
# Definition for a binary tree node.
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

# Function to convert tree to array (level-order traversal)
def tree_to_array(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
sol = Solution()
tree1 = sol.recoverFromPreorder("1-2--3--4-5--6--7")
tree2 = sol.recoverFromPreorder("1-2--3---4-5--6---7")
tree3 = sol.recoverFromPreorder("1-401--349---90--88")

# Print tree as an array
print(tree_to_array(tree1))  # Expected output: [1, 2, 5, 3, 4, 6, 7]
print(tree_to_array(tree2))  # Expected output: [1, 2, 5, 3, None, 6, None, 4, None, 7]
print(tree_to_array(tree3))  # Expected output: [1, 401, None, 349, None, None, 88, 90]