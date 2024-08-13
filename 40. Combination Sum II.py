# i couldnt solve it with two pointer technique 


# from typing import List 
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         print("candidates: ",candidates)
#         left,right=0,len(candidates)-1
#         print("left: ",left, "right: ",right)
#         res_set= set()
#         print(res_set)
#         print("-----befor the loop----")
#         while(left<right):
#             sum = candidates[left]+candidates[right]
#             print("sum: ",sum)
#             if sum>target:
#                 print("sum>target")
#                 right-=1
#                 print("right: ",right)
#             elif sum==target:
#                 print("sum==target")
#                 val=(candidates[left],candidates[right])
#                 print("val: ",val)
#                 print("res_set: ",res_set)
#                 if val not in res_set:
#                     print("val not in res_set")
#                     res_set.add(val)
#                     right-=1
#                     print("res_set: ",res_set)
#                     print("right: ",right)
#             else:
#                 i=0
#                 print("i: ",i)
#                 while candidates[i]+sum<=target:
#                     if candidates[i]+sum==target:
#                         val=(candidates[left],candidates[i],candidates[right])
#                         if val not in res_set:
#                             res_set.add(val)
#                             left+=1
#                             break
#                     i+=1
                
#                 left+=1
#         res=[list(t) for t in res_set]
#         return res



# implimating backtracking 

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        
        candidates.sort()
        res = []
        backtrack(0, target, [])
        return res
                    
res=Solution()
print(res.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))