# class Solution:
#     def findTheLongestSubstring(self, s: str) -> int:
#         vowles = "aeiou"
#         res,mask,mask_to_index =0,0,{0:-1}


#         for i,c in enumerate(s):
#             if c in vowles:
#                 mask = mask^(1+ord(c)-ord('a'))
#             if mask in mask_to_index :
#                 length = i-mask_to_index[mask]
#                 res = max(res,length)
#             else:
#                 mask_to_index[mask]=i
#         return res


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowles ={
            "a":1,
            "e":2,
            "i":4,
            "o":8,
            "u":16
        }
        res,mask,mask_to_index =0,0,[-1]*32


        for i,c in enumerate(s):
           
            mask = mask^vowles.get(c,0)
            if mask_to_index[mask]!=-1 or mask==0 :
                length = i-mask_to_index[mask]
                res = max(res,length)
            else:
                mask_to_index[mask]=i
        return res

sol = Solution()
print(sol.findTheLongestSubstring(s = "eleetminicoworoep"))