class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        if len(s1)> len(s2):
            s1,s2 = s2,s1
        
        left1 , left2 =0,0
        while left1 < len(s1) and left2 < len(s2) and s1[left1] == s2[left2] :
            left1 , left2 = left1 +1 , left2 +1

        right1 , right2 = len(s1)-1 , len(s2)-1
        while right1 >=0 and right2 >= 0 and s1[right1]==s2[right2]:
            right1,right2 = right1-1, right2-1
        
        return left1 > right1