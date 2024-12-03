from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        prev_idx = 0
        for space in spaces:
            res.append(s[prev_idx:space])
            res.append(" ")
            prev_idx = space
        res.append(s[prev_idx:])
        return ''.join(res)

