from typing import List , Optional
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