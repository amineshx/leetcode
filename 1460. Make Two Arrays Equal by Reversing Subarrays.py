from typing import List
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        if arr==target:
            return True
        else :
            return False