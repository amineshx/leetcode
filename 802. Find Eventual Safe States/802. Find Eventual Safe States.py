from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        terminal_node = []
        for node, node_val in enumerate(graph):
            if node_val == []:
                terminal_node.append(node)
        res = terminal_node
        for node, node_val in enumerate(graph):
            for terminal in terminal_node:
                if terminal in node_val:
                    
                    res.append(node)
        res.sort()
        return res


sol = Solution()
print(sol.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))
