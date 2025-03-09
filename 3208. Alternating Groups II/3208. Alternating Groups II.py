from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors.extend(colors[:k-1])  
        count, valid_length = 0, 1  

        for i in range(1, n):
            if colors[i] != colors[i - 1]: 
                valid_length += 1
            else:
                valid_length = 1 
            
            if valid_length >= k:
                count += 1

        return count
