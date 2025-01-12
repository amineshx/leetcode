class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s)%2 != 0:
            return False
        
        locked_count, unlocked_count = 0, 0
        for i in range(len(s)):
            if locked[i] == "0":
                unlocked_count+=1
            elif s[i] =="(":
                locked_count+=1
            else:
                if locked_count:
                    locked_count -=1
                elif unlocked_count:
                    unlocked_count-=1
                else:
                    return False

        if locked_count == 0:
            return True
        
        locked_count, unlocked_count = 0, 0

        for i in reversed(range(len(s))):
            if locked[i]=="0":
                unlocked_count+=1
            elif s[i] ==")":
                locked_count+=1
            else:
                if locked_count:
                    locked_count -=1
                elif unlocked_count:
                    unlocked_count-=1
                else:
                    return False
        
        return True
