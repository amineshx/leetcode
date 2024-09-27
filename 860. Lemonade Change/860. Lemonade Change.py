from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=ten=0

        for b in bills:
            if b==5:
                five+=1
            if b==10:
                ten+=1
            
            change=b-5
            if change ==5 :
                if five >0:
                    five-=1
                else :
                    return False
            elif change==15:
                if ten>0 :
                    if five>0:
                        ten-=1
                        five-=1
                    else :
                        return False
                else :
                    if five>=3:
                        five-=3
                    else :
                        return False
        return True