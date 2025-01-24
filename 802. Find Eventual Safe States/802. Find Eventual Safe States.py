from typing import List
# sol1 dosn't pass all test cases
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        terminal_node = []
        for node, node_val in enumerate(graph):
            if node_val == []:
                terminal_node.append(node)
        res = terminal_node
        for node, node_val in enumerate(graph):
            for terminal in terminal_node:
                if terminal in node_val and len(node_val)==1:
                    
                    res.append(node)
        res.sort()
        return res



# sol 2 
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n  
        
        def dfs(node: int) -> bool:
            if color[node] > 0:
                return color[node] == 2
            
            color[node] = 1  
            for neighbor in graph[node]:
                if color[neighbor] == 2:
                    continue
                if color[neighbor] == 1 or not dfs(neighbor):
                    return False
            
            color[node] = 2  
            return True
        
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res

sol = Solution()
print(sol.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))