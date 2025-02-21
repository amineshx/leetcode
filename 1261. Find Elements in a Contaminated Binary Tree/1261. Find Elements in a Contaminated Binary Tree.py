from typing import Optional , List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.recoveredValues = set()
        root.val = 0
        self.recoverTree(root)

    def recoverTree(self, root: Optional[TreeNode]):
        if not root:
            return
        self.recoveredValues.add(root.val)
        if root.left:
            root.left.val = 2*root.val+1
            self.recoverTree(root.left)
        if root.right:
            root.right.val = 2*root.val+2
            self.recoverTree(root.right)

    def find(self, target: int) -> bool:
        return target in self.recoveredValues


# Function to construct the tree from the list representation
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while i < len(nodes):
        current = queue.pop(0)
        
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        
        i += 1

    return root

# Function to test with a given example input
def test_find_elements(operations: List[str], values: List[List[Optional[int]]]):
    root_list = values[0][0]  # Extract tree representation
    root = build_tree(root_list)  # Build the tree

    find_elements = FindElements(root)  # Instantiate the class
    results = [None]  # First operation is always instantiation

    for i in range(1, len(operations)):
        if operations[i] == "find":
            results.append(find_elements.find(values[i][0]))

    return results

# Example 1
operations1 = ["FindElements", "find", "find"]
values1 = [[[-1, None, -1]], [1], [2]]
print(test_find_elements(operations1, values1))  # Expected output: [None, False, True]

# Example 2
operations2 = ["FindElements", "find", "find", "find"]
values2 = [[[-1, -1, -1, -1, -1]], [1], [3], [5]]
print(test_find_elements(operations2, values2))  # Expected output: [None, True, True, False]

# Example 3
operations3 = ["FindElements", "find", "find", "find", "find"]
values3 = [[[-1, None, -1, -1, None, -1]], [2], [3], [4], [5]]
print(test_find_elements(operations3, values3))  # Expected output: [None, True, False, False, True]