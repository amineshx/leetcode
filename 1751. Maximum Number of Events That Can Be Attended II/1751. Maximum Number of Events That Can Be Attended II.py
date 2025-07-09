from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)

        start_times = [e[0] for e in events]
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]

            prev = self.findLastNonOverlapping(events, i - 1, start)

            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[prev + 1][j - 1] + value)

        return dp[n][k]

    def findLastNonOverlapping(self, events, right, targetStart):
        left = 0
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if events[mid][1] < targetStart:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res