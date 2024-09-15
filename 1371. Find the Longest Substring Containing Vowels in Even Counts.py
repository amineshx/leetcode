class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowles = "aeiou"
        res,mask,mask_to_index =0,0,{0:-1}


        for i,c in enumerate(s):
            if c in vowles:
                mask = mask^(1+ord(c)-ord('a'))
            if mask in mask_to_index :
                length = i-mask_to_index[mask]
                res = max(res,length)
            else:
                mask_to_index[mask]=i
        return res