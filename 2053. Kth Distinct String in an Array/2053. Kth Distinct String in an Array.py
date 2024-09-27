from typing import List
from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = Counter(arr)
        unique_chars_in_order = [char for char in arr if count_dict[char] == 1]
        if 0 <= k - 1 < len(unique_chars_in_order):
            return unique_chars_in_order[k - 1]
        else:
            return ""

res=Solution()
print(res.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))
        