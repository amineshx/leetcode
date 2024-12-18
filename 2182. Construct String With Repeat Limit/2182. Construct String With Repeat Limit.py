from collections import Counter
import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        
        max_heap=[(-ord(char), cnt) for char, cnt in count.items()]
        heapq.heapify(max_heap)
        res=[]
        while max_heap:
            char,cnt = heapq.heappop(max_heap)
            char = chr(-char)
            current_count = min(cnt,repeatLimit)
            res.append(char*current_count)

            if cnt-current_count>0 and max_heap:
                next_char, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char)
                res.append(next_char)
                if next_count>1:
                    heapq.heappush(max_heap,(-ord(next_char), next_count-1))
                heapq.heappush(max_heap,(-ord(char), cnt-current_count))
        
        return "".join(res)

