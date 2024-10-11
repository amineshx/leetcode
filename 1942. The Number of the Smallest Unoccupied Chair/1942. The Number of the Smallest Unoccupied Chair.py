from typing import List
import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [ (time[0],time[1],i) for i,time in enumerate(times)]
        times.sort()
        used_chairs = []
        avaliable_chairs = [i for i in range(len(times))]

        for a,l,i in times:
            while used_chairs and used_chairs[0][0] <=a:
                leave, chair = heapq.heappop(used_chairs)
                heapq.heappush(avaliable_chairs,chair)
            chair = heapq.heappop(avaliable_chairs)
            heapq.heappush(used_chairs,(l,chair))
            if i == targetFriend:
                return chair


sol = Solution()
print(sol.smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 1))