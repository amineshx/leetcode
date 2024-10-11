from typing import List
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [ (time[0],time[1],i) for i,time in enumerate(times)]
        times.sort()
        used_chairs = []
        avaliable_chairs = [i for i in range(len(times))]

        return avaliable_chairs

sol = Solution()
print(sol.smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 1))