// from typing import List
// from collections import deque,defaultdict
// class Solution:
//     def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
//         adj=defaultdict(list)
//         for v1,v2 in edges:
//             adj[v1].append(v2)
//             adj[v2].append(v1)
//         q=deque([1])
//         current_time=0
//         res =-1
//         visit_times=defaultdict(list)   
//         while q:
//             for _ in range(len(q)):
//                 node = q.popleft()
//                 if node ==n:
//                     if res !=-1:
//                         return current_time
//                     res = current_time
//                 for nei in adj[node]:
//                     nei_times=visit_times[nei]
//                     if len(nei_times)==0 or (len(nei_times)==1 and nei_times[0]!=current_time):
//                         q.append(nei)
//                         nei_times.append(current_time)
//             if(current_time//change)%2==1:
//                 current_time+=change-(current_time%change)
//             current_time+=time

// sol = Solution()
// print(sol.secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))

// #sol 2

// class Solution:

//     def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
//         g = [[] for _ in range(n + 1)]
//         for u, v in edges:
//             g[u].append(v)
//             g[v].append(u)

//         q = deque([(1, 1)])
//         dist1 = [-1] * (n + 1)
//         dist2 = [-1] * (n + 1)
//         dist1[1] = 0
//         while q:
//             x, freq = q.popleft()
//             t = dist1[x] if freq == 1 else dist2[x]
//             if (t // change) % 2:
//                 t = change * (t // change + 1) + time
//             else:
//                 t += time
//             for y in g[x]:
//                 if dist1[y] == -1:
//                     dist1[y] = t
//                     q.append((y, 1))
//                 elif dist2[y] == -1 and dist1[y] != t:
//                     if y == n:
//                         return t
//                     dist2[y] = t
//                     q.append((y, 2))
//         return 0

        

var secondMinimum = function(n, edges, time, change) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u - 1].push(v - 1);
        adj[v - 1].push(u - 1);
    }
    
    const dist = Array.from({ length: n }, () => [Number.MAX_SAFE_INTEGER, Number.MAX_SAFE_INTEGER]);
    dist[0][0] = 0;
    
    const q = [[0, 0]];
    
    while (q.length > 0) {
        const [currTime, node] = q.shift();
        
        for (const adjNode of adj[node]) {
            let waitingTime = 0;
            if (Math.floor(currTime / change) % 2 === 1) {
                waitingTime = change - (currTime % change);
            }
            
            const newTime = time + currTime + waitingTime;
            
            if (dist[adjNode][0] > newTime) {
                dist[adjNode][1] = dist[adjNode][0];
                dist[adjNode][0] = newTime;
                q.push([newTime, adjNode]);
            } else if (dist[adjNode][1] > newTime && dist[adjNode][0] < newTime) {
                dist[adjNode][1] = newTime;
                q.push([newTime, adjNode]);
            }
        }
    }
    
    return dist[n-1][1];
};

console.log(secondMinimum( n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))