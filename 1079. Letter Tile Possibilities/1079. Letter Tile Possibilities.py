from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtracking(counter):
            res = 0
            for char in counter:
                if counter[char]>0:
                    res+=1
                    counter[char]-=1
                    res+=backtracking(counter)
                    counter[char]+=1
            return res
        
        counnter = Counter(tiles)
        return backtracking(counnter)