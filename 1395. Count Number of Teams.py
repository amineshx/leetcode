from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res =0
        for mid in range(1,len(rating)-1):
            left_min=right_max=0
            for i in range(mid):
                if rating[i]<rating[mid]:
                    left_min+=1

            for i in range(mid+1,len(rating)):
                if rating[i]>rating[mid]:
                    right_max+=1
            res+=left_min*right_max

            left_max=mid-left_min
            right_min=len(rating)-mid-1-right_max
            res+=left_max*right_min

        return res