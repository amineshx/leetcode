from typing import List , Optional
from collections import deque   # has no relation with challenge , just to visualize the tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        postorder_to_hash_map = {}

        for i,val in enumerate(postorder):
            postorder_to_hash_map[val]=i
        
        def buid_tree(idx1,idx2,jdx1,jdx2):
            if idx1>idx2 or jdx1>jdx2:
                return None
            root = TreeNode(preorder[idx1])
            if idx1!=idx2:
                left_val = preorder[idx1+1]
                mid = postorder_to_hash_map[left_val]
                window_size = mid - jdx1 +1
                root.left = buid_tree(idx1+1, idx1+ window_size, jdx1, mid)
                root.right = buid_tree(idx1+window_size+1, idx2, mid+1, jdx2-1)
            return root


        return buid_tree(0,n-1,0,n-1)
    



# Function to convert tree to array (level-order traversal)
def tree_to_array(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    res = []
    q = deque([root])

    while q:
        node = q.popleft()

        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    
    # Remove trailing None values
    while res and res[-1] is None:
        res.pop()
    return res 

sol = Solution()
tree1 = sol.constructFromPrePost(preorder=[1,2,4,5,3,6,7], postorder=[4,5,2,6,7,3,1])
tree2 = sol.constructFromPrePost(preorder=[1], postorder=[1])

# Print tree as an array
print(tree_to_array(tree1))  # Expected output: [1, 2, 3, 4, 5, 6, 7]
print(tree_to_array(tree2))  # Expected output: [1]

    