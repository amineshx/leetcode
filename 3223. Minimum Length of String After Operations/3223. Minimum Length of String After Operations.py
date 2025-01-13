from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if freq % 2 else 2 for freq in Counter(s).values())