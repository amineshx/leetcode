class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        i=0
        while i <len(sentence)-1:
            if sentence[i]==" " and i!= 0:
                if sentence[i-1]!=sentence[i+1]:
                    return False
            i+=1

        if sentence[0]!=sentence[-1]:
            return False
        return True

