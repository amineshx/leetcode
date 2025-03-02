from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i=j=0
        res = []

        while i<len(nums1) and j<len(nums2):
            if nums1[i][0] > nums2[j][0]:
                res.append(nums2[j])
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i+=1
            else:
                idi = nums1[i][0]
                val = nums1[i][1]+nums2[j][1]
                res.append([idi,val])
                i+=1
                j+=1
        
        while i<len(nums1):
            res.append(nums1[i])
            i+=1
        
        while j<len(nums2):
            res.append(nums2[j])
            j+=1
        
        return res

sol = Solution()
print(sol.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))
print(sol.mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]))