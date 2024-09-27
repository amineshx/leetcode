# import heapq
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         minHeap=[1] # init the minheap with the first ugly num which is 1
#         visited=set()
#         prim_factors=[2,3,5]    

#         for i in range(n):
#             res=heapq.heappop(minHeap)
#             if i == n-1:
#                 return res
            
#             for j in  prim_factors:
#                 num= res*j
#                 if num not in visited:
#                     visited.add(num)
#                     heapq.heappush(minHeap,num)


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[1]
        j,k,l=0,0,0

        for i in range(1,n):
            nxt=min(nums[j]*2,nums[k]*3,nums[l]*5)
            nums.append(nxt)
            if nums[j]*2==nxt:
                j+=1
            if nums[k]*3==nxt:
                k+=1
            if nums[l]*5==nxt:
                l+=1
        
        return nums[n-1]