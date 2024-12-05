class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if target == start:
            return True 
        left = right = 0

        for current, goal in zip(start, target):
            if current == 'R':
                if left>0:
                    return False
                right+=1
            if goal == 'L':
                if right>0:
                    return False
                left+=1
            if goal == 'R':
                if right==0:
                    return False
                right-=1
            if current == 'L':
                if left == 0:
                    return False
                left-=1
        return left==0 and right==0
