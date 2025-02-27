from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        set_of_arr = set(arr)
        res = 0

        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                prev_pointer = arr[i]
                cur_pointer = arr[j]
                nex_pointer = prev_pointer+cur_pointer
                length=2
                while nex_pointer in set_of_arr:
                    length+=1
                    prev_pointer,cur_pointer = cur_pointer,nex_pointer
                    nex_pointer=prev_pointer+cur_pointer
                    res = max(res,length)
        return res

sol = Solution()
print(sol.lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8]))
print(sol.lenLongestFibSubseq(arr = [1,3,7,11,12,14,18]))