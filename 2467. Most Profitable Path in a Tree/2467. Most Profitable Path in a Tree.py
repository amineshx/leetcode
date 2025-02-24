from typing import List
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = {i: [] for i in range(len(amount))}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobPath = [-1] * len(amount)
        path = []

        def fillBobPath(node, parent):
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    path.append(node)
                    if fillBobPath(neighbor, node):
                        return True
                    path.pop()

        fillBobPath(bob, -1)
        for i, node in enumerate(path):
            bobPath[node] = i
        
        def getAliceMaxScore(node, parent, currScore, timestamp):
            if bobPath[node] == -1 or bobPath[node] > timestamp:
                currScore += amount[node]
            elif bobPath[node] == timestamp:
                currScore += amount[node] // 2
            return currScore if len(graph[node]) == 1 and node != 0 else max(getAliceMaxScore(neighbor, node, currScore, timestamp + 1) for neighbor in graph[node] if neighbor != parent)

        return getAliceMaxScore(0, -1, 0, 0)

sol = Solution()
print(sol.mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]))
print(sol.mostProfitablePath(edges = [[0,1]], bob = 1, amount = [-7280,2350]))