from typing import List
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n=len(events)

        min_heap = []
        i=0
        res=0
        last_day = events[0][1]
        for _,endev in events:
            last_day=max(last_day,endev)
        
        for day in range(1, last_day + 1):
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                res += 1
            if i == n and not min_heap:
                break


        return res

sol = Solution()
print(sol.maxEvents(events= [[1,2],[2,3],[3,4],[1,2]]))
print(sol.maxEvents(events = [[1,2],[2,3],[3,4]]))