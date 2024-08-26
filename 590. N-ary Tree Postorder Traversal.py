from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

    def __repr__(self):
        return f"Node({self.val})"

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        print("stack: ", stack)
        res = []

        while stack:
            node = stack.pop()
            print("node: ",node)
            print("stack: ", stack)
            print("node val: ",node.val)
            res.append(node.val)
            stack.extend(node.children)
            print("node children : ",node.children)
            print("stack: ", stack)
            print("res: ", res)
        return res[::-1]

root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

sol = Solution()
print(sol.postorder(root))
